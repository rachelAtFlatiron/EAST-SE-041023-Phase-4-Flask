import { useFormik } from "formik";
import * as yup from "yup";
import { useHistory } from "react-router-dom";

function ActorForm() {
	const history = useHistory();

	const schema = yup.object().shape({
		name: yup.string().required("required"),
		age: yup.number().positive("must be positive"),
		image: yup.string().required("required"),
		country: yup.string(),
	});

	const formik = useFormik({
		initialValues: {
			name: "",
			age: 0,
			country: "",
			image: "",
		},
		validationSchema: schema,
		onSubmit: (values) => {
			console.log(values);
			fetch("/actors", {
				method: "POST",
				headers: {
					"content-type": "application/json",
				},
				body: JSON.stringify(values),
			}).then((res) => {
				if (res.ok) {
					res.json().then((actor) => {
						console.log(actor);
						history.push(`/actors/${actor.id}`);
					});
				}
			});
		},
	});
	return (
		<section>
			<form className="form">
				<label>Full Name </label>

				<input
					type="text"
					name="name"
					value={formik.values.name}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.name && formik.errors.name ? (
					<h3 style={{ color: "red" }}>{formik.errors.name}</h3>
				) : (
					""
				)}
				<label>Image </label>

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
				<label>Age </label>

				<input
					type="text"
					name="age"
					value={formik.values.age}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.age && formik.errors.age ? (
					<h3 style={{ color: "red" }}>{formik.errors.age}</h3>
				) : (
					""
				)}
				<label>Country </label>
				<input
					type="text"
					name="country"
					value={formik.values.country}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ActorForm;
