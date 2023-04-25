import { Link } from "react-router-dom";

function Navigation() {
	return (
		<header>
			<h1>
				<Link to={"/"}>
					{"//"} Not the Oscars
				</Link>
			</h1>

			<div className="menu">
				<Link className="button" to="/">
					All Productions
				</Link>
				<Link className="button" to={"/actors"}>
					All Actors
				</Link>
				<Link className="button" to={"/actors/new"}>
					New Actor
				</Link>
				<Link className="button" to="/productions/new">
					New Production
				</Link>
			</div>
		</header>
	);
}

export default Navigation;
