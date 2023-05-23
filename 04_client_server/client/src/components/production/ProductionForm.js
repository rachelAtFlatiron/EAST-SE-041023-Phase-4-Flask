import { redirect } from "react-router-dom";
// 4a. Import useFormik and yup
import { useFormik } from "formik";
import * as yup from "yup";

function ProductionForm() {

	// 4b. create yup schema where:
	// title: required
	// length: must be positive
	// year is a minimum of 1850
	// image: required
	// description: max length is 250
	const schema = yup.object().shape({
		title: yup.string().required("required"),
		genre: yup.string(),
		length: yup.number().positive("must be positive"),
		year: yup.number().min(1850, "were cameras even a thing that long ago?"),
		image: yup.string().required("required"),
		language: yup.string(),
		director: yup.string(),
		description: yup.string().max(250, "too long"),
		composer: yup.string(),
	});

	// 4c. create formik with...
	const formik = useFormik({
		// 4c. ...initial values of form...
		initialValues: {
			title: "",
			genre: "",
			length: 0,
			year: 0,
			image: "",
			language: "",
			director: "",
			description: "",
			composer: "",
		},
		// 4c...yup schema for validation....
		validationSchema: schema,
		// 4c. submit callback
		onSubmit: (values) => {
			console.log(values);
			fetch("/productions", {
				method: "POST",
				headers: {
					"content-type": "application/json",
				},
				body: JSON.stringify(values),
			}).then((res) => {
				if (res.ok) {
					res.json().then((production) => {
						console.log(production);
						redirect(`/productions/${production.id}`);
					});
				} else {
					res.json().then((err) => console.log("oops"));
				}
			});
		},
	});

	return (
		<section>
			{/* 5a. attach formik submit handler to form */}
			<form onSubmit={formik.handleSubmit} className="form">
				<label>Title </label>
				<input
					type="text"
					name="title"
					// 5b. attach formik change handler to inputs 
					onChange={formik.handleChange}
					// 5c. pass in formik values to make form controlled
					value={formik.values.title}
					// 6a. add onBlur event to allow formik to update "formik.touched"
					onBlur={formik.handleBlur}
				/>
				{/* 6b. use formik.touched and formik.errors to render errors where needed */}
				{formik.touched.title && formik.errors.title ? (
					<h3>{formik.errors.title}</h3>
				) : (
					""
				)}

				<label> Genre</label>
				<input
					type="text"
					name="genre"
					value={formik.values.genre}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>

				<label>Length</label>
				<input
					type="number"
					name="length"
					value={formik.values.length}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.length && formik.errors.length ? (
					<h3 style={{ color: "red" }}>{formik.errors.length}</h3>
				) : (
					""
				)}

				<label>Year</label>
				<input
					type="number"
					name="year"
					value={formik.values.year}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.year && formik.errors.year ? (
					<h3 style={{ color: "red" }}>{formik.errors.year}</h3>
				) : (
					""
				)}

				<label>Image</label>
				<input
					type="text"
					name="image"
					value={formik.values.image}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.image && formik.errors.image ? (
					<h3 style={{ color: "red" }}>{formik.errors.image}</h3>
				) : (
					""
				)}
				<label>Language</label>
				<input
					type="text"
					name="language"
					value={formik.values.language}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>

				<label>Director</label>
				<input
					type="text"
					name="director"
					value={formik.values.director}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>

				<label>Description</label>
				<textarea
					type="text"
					rows="4"
					cols="50"
					name="description"
					value={formik.values.description}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.description && formik.errors.description ? (
					<h3 style={{ color: "red" }}>{formik.errors.description}</h3>
				) : (
					""
				)}
				<label>Composer</label>
				<input
					type="text"
					name="composer"
					value={formik.values.composer}
					onChange={formik.handleChange}
				/>

				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ProductionForm;
