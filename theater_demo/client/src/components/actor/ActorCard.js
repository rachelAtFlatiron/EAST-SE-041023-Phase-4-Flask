import { Link } from "react-router-dom";

function ActorCard({ actor }) {
    const { name, image, country, age, id } = actor;

  return (
    <li className="card" id={id}>
    <figure className="image">
        <img src={image} alt={name} />
    </figure>
    <section className="details">
        <Link to={`/actors/${id}`}>
            <h2>{name}</h2>
        </Link>
        <p>{age}, {country}</p>
    </section>
</li>
  )
}

export default ActorCard