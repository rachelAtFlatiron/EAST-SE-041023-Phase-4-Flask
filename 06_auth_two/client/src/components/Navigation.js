import { Link, NavLink, useNavigate } from "react-router-dom";

function Navigation({ updateUser, user }) {
	const navigate = useNavigate();

	function handleLogout() {
		fetch("/logout").then((res) => {
			if (res.ok){
				updateUser(null);
				navigate("/auth");
			}
		});
	}

	return (
		<header>
			<h1>
				<Link to={"/"}>{"//"} Not the Oscars</Link>
			</h1>

			<div className="menu">
				<NavLink className="button" to="/productions" end>
					All Productions
				</NavLink>
				<NavLink className="button" to="/actors" end>
					All Actors
				</NavLink>
				<NavLink className="button" to="/actors/new">
					New Actor
				</NavLink>
				<NavLink className="button" to="/productions/new">
					New Production
				</NavLink>
				<NavLink className="button" to="/auth">
					Log In
				</NavLink>
				{ user ? 
					(<>
						<button onClick={handleLogout} className="button">
							Log Out
						</button>
						<p style={{'margin-top': '8px'}}>Hello, {user.username}</p>
					</>) : 
					''
				}		
			</div>
		</header>
	);
}

export default Navigation;
