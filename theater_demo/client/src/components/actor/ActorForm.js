function ActorForm() {
	// 8. use formik and yup to create actor form
	return (
		<section>
			<form onSubmit={() => {}} className="form">

				<label>Full Name </label>
				<input
					type="text"
					name="name"
				/>

				<label>Image </label>
				<input
					type="text"
					name="image"
				/>

				<label>Age </label>
				<input
					type="text"
					name="age"
				/>

				<label>Country </label>
				<input
					type="text"
					name="country"
				/>
				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ActorForm;
