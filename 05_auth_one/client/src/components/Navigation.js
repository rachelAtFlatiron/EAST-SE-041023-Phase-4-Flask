import { Link, NavLink, useNavigate } from "react-router-dom";

// 11a. pass down user as props
function Navigation({ updateUser, user }) {
	const navigate = useNavigate();

	// ** You Do **
	// 6a. write logout function that fetches `/logout`
	function handleLogout() {
		fetch("/logout").then((res) => {
			// 6b. if res.ok....
			if (res.ok){
				// 6b. update the user to be no one....
				updateUser(null);
				// 6c. navigate to the login page
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
