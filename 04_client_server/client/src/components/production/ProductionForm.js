// 4a. Import useFormik and yup

function ProductionForm() {

	// 4b. create yup schema where:
	// title: required
	// length: must be positive
	// year is a minimum of 1850
	// image: required
	// description: max length is 250

	// 4c. create formik with...
		// 4c. ...initial values of form...
		// 4c...yup schema for validation....
		// 4c. submit callback

	return (
		<section>
			{/* 5a. attach formik submit handler to form */}
			<form onSubmit={() => {}} className="form">
				<label>Title </label>
				<input
					type="text"
					name="title"
					// 5b. attach formik change handler to inputs 
					// 5c. pass in formik values to make form controlled
					// 6a. add onBlur event to allow formik to update "formik.touched"
				/>
				{/* 6b. use formik.touched and formik.errors to render errors where needed */}

				<label> Genre</label>
				<input
					type="text"
					name="genre"
				/>

				<label>Length</label>
				<input
					type="number"
					name="length"
				/>

				<label>Year</label>
				<input
					type="number"
					name="year"
				/>

				<label>Image</label>
				<input
					type="text"
					name="image"
				/>

				<label>Language</label>
				<input
					type="text"
					name="language"
				/>

				<label>Director</label>
				<input
					type="text"
					name="director"
				/>

				<label>Description</label>
				<textarea
					type="text"
					rows="4"
					cols="50"
					name="description"
				/>

				<label>Composer</label>
				<input
					type="text"
					name="composer"
				/>

				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ProductionForm;
