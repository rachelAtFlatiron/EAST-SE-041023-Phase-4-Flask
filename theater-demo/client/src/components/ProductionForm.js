import { useHistory } from "react-router-dom";

import { useFormik } from "formik";
import * as yup from "yup";

function ProductionForm() {
	const history = useHistory();

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

	// const initialValues = {
	// 	title: '',
	// 	genre: '',
	// 	length: 0,
	// 	year: 0,
	// 	image: '',
	// 	language: '',
	// 	director: '',
	// 	description: '',
	// 	composer: ''
	// }

	const formik = useFormik({
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
		validationSchema: schema,
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
						history.push(`/productions/${production.id}`);
					});
				} else {
					res.json().then((err) => console.log("oops"));
				}
			});
		},
	});

	return (
		<section>
			<form onSubmit={formik.handleSubmit} className="form">
				<label>Title </label>
				<input
					type="text"
					name="title"
					value={formik.values.title}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
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
