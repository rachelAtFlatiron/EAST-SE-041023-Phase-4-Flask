import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import Home from "./components/Home";
import Navigation from "./components/Navigation";
import NotFound from "./components/NotFound";
import ActorForm from "./components/actor/ActorForm";
import ActorContainer from "./components/actor/ActorContainer";
import ActorDetail from "./components/actor/ActorDetail";
import ProductionContainer from "./components/production/ProductionContainer";
import ProductionForm from "./components/production/ProductionForm";
import ProductionDetail from "./components/production/ProductionDetail";
import Auth from "./components/Auth";

function App() {
	const [productions, setProductions] = useState([]);
	const [actors, setActors] = useState([]);
	const [user, setUser] = useState(null)

	useEffect(() => {
		fetch("/productions")
			.then((res) => res.json())
			.then(setProductions);
		fetch("/actors")
			.then((res) => res.json())
			.then(setActors);
		getUser()
	}, []);

	const updateUser = (user) => {
		setUser(user)
	}

	const getUser = () => {
		fetch('/authorized-session')
		.then(res => {
			if(res.ok){
				res.json().then(data => {
					setUser(data)
				})
			} else {
				setUser(null)
			}
		})
	}

	const addProduction = (production) =>
		setProductions((current) => [...current, production]);
	
	// here is what we render if there is no user
	if (!user){
		return (
			<div className="App light">
				<Navigation updateUser={updateUser} user={user} />
				<Auth updateUser={updateUser} />
			</div>
		)
	}
	return (
		<div className="App light">
			<Navigation updateUser={updateUser} user={user} />
			<Routes>
				< Route path = "/auth" element={<Auth updateUser={updateUser} />} />

				<Route path="/actors/new" element={<ActorForm />} />

				<Route path="/productions/new" element={<ProductionForm addProduction={addProduction} />} />
				
				<Route path="/productions/:id" element={<ProductionDetail />} />

				<Route path="/productions" element={<ProductionContainer productions={productions} />} />

				<Route path="/actors/:id" element={<ActorDetail />} />

				<Route path="/actors" element={<ActorContainer actors={actors} />} />

				<Route path="/not-found" element={<NotFound />} />

				<Route exact path="/" element={<Home />} />
			</Routes>
		</div>
	);
}

export default App;
