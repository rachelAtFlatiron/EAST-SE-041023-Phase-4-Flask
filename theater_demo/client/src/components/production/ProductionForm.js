// 5a. Import useFormik and yup
import { useFormik } from "formik"
import { useNavigate } from "react-router-dom"
import * as yup from "yup"

// useEffect triggers get request -> sends request to flask/app.py -> app.py runs GET method -> returns response/error back to react

// formik onSubmit -> triggered by clicking submit button -> sends request to flask -> runs POST method in app.py -> returns either response or error

function ProductionForm() {

	const navigate = useNavigate()

	// 5b. create yup schema where:
	// title: required
	// length: must be positive
	// year is a minimum of 1850
	// image: required
	// description: max length is 250
	const schema = yup.object().shape({
		title: yup.string().required('title is required'),
		genre: yup.string(),
		image: yup.string().required('image is required'),
		director: yup.string(),
		description: yup.string().max(250, 'must be less than 250 characters'),
		composer: yup.string(),
		year: yup.number().min(1850, "must be greater than 1850"),
		length: yup.number().positive("must be positive")
	})

	// 5c. create formik with...
	const formik = useFormik({
		// 5c. ...initial values of form...
		initialValues:{
			title: '',
			genre: '',
			length: 0,
			year: 1850,
			image: '',
			language: '',
			director: '',
			description: '',
			composer: ''
		},
		// 5c...yup schema for validation....
		validationSchema: schema,
		// 5c. submit callback
		onSubmit: (values) => {
			fetch("/productions", {
				method: 'POST',
				headers: {
					'content-type': 'application/json'
				},
				body: JSON.stringify(values)
			}).then(res => {
				if(res.ok){
					res.json().then(production => {
						console.log(production)
						navigate(`/productions/${production.id}`)
					})
				} else {
					console.log('oops')
				}
			})
		}
	})

	return (
		<section>
			{/* 6a. attach formik submit handler to form */}
			<form onSubmit={formik.handleSubmit} className="form">
				<label>Title </label>
				<input
					type="text"
					name="title"
					// 6b. attach formik change handler to inputs 
					onChange={formik.handleChange}
					// 6c. pass in formik values to make form controlled
					value={formik.values.title}
					// 7a. add onBlur event to allow formik to update "formik.touched"
					onBlur={formik.handleBlur}
				/>
				{/* 7b. use formik.touched and formik.errors to render errors where needed */}
				{formik.touched.title && formik.errors.title ? (
					<h3>{formik.errors.title}</h3>	
				) : ('')}

				<label> Genre</label>
				<input
					type="text"
					name="genre"
					onChange={formik.handleChange}
					value={formik.values.genre}
				/>

				<label>Length</label>
				<input
					type="number"
					name="length"
					onChange={formik.handleChange}
					value={formik.values.length}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.length && formik.errors.length ? (
					<h3>{formik.errors.length}</h3>	
				) : ('')}

				<label>Year</label>
				<input
					type="number"
					name="year"
					onChange={formik.handleChange}
					value={formik.values.year}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.year && formik.errors.year ? (
					<h3>{formik.errors.year}</h3>	
				) : ('')}

				<label>Image</label>
				<input
					type="text"
					name="image"
					onChange={formik.handleChange}
					value={formik.values.image}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.image && formik.errors.image ? (
					<h3>{formik.errors.image}</h3>	
				) : ('')}

				<label>Language</label>
				<input
					type="text"
					name="language"
					onChange={formik.handleChange}
					value={formik.values.language}
				/>

				<label>Director</label>
				<input
					type="text"
					name="director"
					onChange={formik.handleChange}
					value={formik.values.director}
				/>

				<label>Description</label>
				<textarea
					type="text"
					rows="4"
					cols="50"
					name="description"
					onChange={formik.handleChange}
					value={formik.values.description}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.description && formik.errors.description ? (
					<h3>{formik.errors.description}</h3>	
				) : ('')}

				<label>Composer</label>
				<input
					type="text"
					name="composer"
					onChange={formik.handleChange}
					value={formik.values.composer}
				/>

				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ProductionForm;
