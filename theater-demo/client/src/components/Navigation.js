import { Link, NavLink } from "react-router-dom";

function Navigation() {
	return (
		<header>
			<h1>
				<Link to={"/"}>
					{"//"} Not the Oscars
				</Link>
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
			</div>
		</header>
	);
}

export default Navigation;
