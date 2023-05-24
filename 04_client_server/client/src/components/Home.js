import { useState, useEffect } from "react";
import ProductionCard from "./production/ProductionCard";

function Home() {
	// 2a. create state for the longest movies
	// 2b. use useEffect to fetch /longest-movies and update state

	return (
		<div>
			<section>
				<h2>Longest Movies</h2>
			</section>
			<ul
				style={{
					display: "flex",
					flexWrap: "wrap",
					justifyContent: "center",
				}}
			>
				{[].map((el) => (
					<section style={{ display: "flex", flexDirection: "column" }}>
						<h3>{el.length} minutes</h3>

						<ProductionCard key={el.id} production={el} />
					</section>
				))}
			</ul>

			<section>
				<h2>Most Popular Actors</h2>
			</section>
		</div>
	);
}

export default Home;
