import { useParams, redirect, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function ActorDetail() {
	const [actor, setActor] = useState({
		roles: [],
	});

	// 4a. fetch current actor based on params
	const params = useParams() //params.id
	const navigate = useNavigate()
	// 4a. save actor data in state
	useEffect(() => {
		fetch(`/actors/${params.id}`).then((res) => {
			// 4c. if response is not ok, navigate to /not-found
			if(res.ok){
				res.json().then(data => setActor(data))
			} else {
				//navigate come from react-router
				//so we know that this is a front-end route
				navigate('/not-found')
			}
		})
	}, [])

	// 4b. destructure the values and display them on page
	const { id, name, age, country, image } = actor;

	return (
		<div className="project-detail" id={id}>
			<h1>{name}</h1>
			<div className="project-card">
				<figure className="image">
					<img width={"300px"} src={image} alt={name} />
				</figure>
				<section className="details">
					<h3 style={{ margin: "16px auto" }}>Productions: </h3>
					<ul className="crew">
						{actor.roles.map((role) => (
							<li>
								<img
									width={"100px"}
									src={role.production.image}
									alt={role.production.title}
								/>
								<div className="crew-member">
									<Link to={`/productions/${role.production.id}`}>
										<p style={{ "font-style": "italic" }}>
											{role.production.title}
										</p>
									</Link>
									<p>{role.role_name}</p>
								</div>
							</li>
						))}
					</ul>
				</section>
			</div>
		</div>
	);
}

export default ActorDetail;
