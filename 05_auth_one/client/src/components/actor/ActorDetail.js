import { useParams, redirect, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function ActorDetail() {
	const [actor, setActor] = useState({
		roles: [],
	});

	const params = useParams();
	const navigate = useNavigate();
	useEffect(() => {
		fetch(`/actors/${params.id}`).then((res) => {
			if (res.ok) {
				res.json().then((data) => setActor(data));
			} else {
				navigate('/not-found')
			}
		});
	}, []);

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
