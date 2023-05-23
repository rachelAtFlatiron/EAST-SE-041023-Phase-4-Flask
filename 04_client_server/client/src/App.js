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

function App() {
	const [productions, setProductions] = useState([]);
	const [actors, setActors] = useState([]);

	// 2a. create a useEffect to fetch from /productions and /actors
	useEffect(() => {
		// 2b. save the result in state
		fetch("/productions")
			.then((res) => res.json())
			.then(setProductions);
		fetch("/actors")
			.then((res) => res.json())
			.then(setActors);
	}, []);

	const addProduction = (production) =>
		setProductions((current) => [...current, production]);

	return (
		<div className="App light">
			<Navigation />
			<Routes>
				<Route path="/actors/new" element={<ActorForm />} />

				<Route path="/productions/new" element={<ProductionForm addProduction={addProduction} />}
				/>
				<Route path="/productions/:id" element={<ProductionDetail />} />

				{/* 2c. pass productions here down  */}
				<Route path="/productions" element={<ProductionContainer productions={productions} />} />

				<Route path="/actors/:id" element={<ActorDetail />} />

				{/* 2c. pass actors here down  */}
				<Route path="/actors" element={<ActorContainer actors={actors} />} />
				<Route path="/not-found" element={<NotFound />} />

				<Route exact path="/" element={<Home />} />
			</Routes>
		</div>
	);
}

export default App;
