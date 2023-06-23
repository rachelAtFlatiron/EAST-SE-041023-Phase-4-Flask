import { useNavigate } from 'react-router-dom'
import { useState } from "react";
import { useFormik } from 'formik'
import * as yup from 'yup'

function Auth({ updateUser }) {
	const [signup, setSignup] = useState(true);
    const navigate = useNavigate()
	const toggleSignup = () => setSignup((prev) => !prev);

    // 3a. create a validations schema using yup
	const formSchema = yup.object().shape({
		name: yup.string(),
		username: yup.string().required("Please enter username")
	})
    // 3b. create a formik instance containing...
	const formik = useFormik({
		// 3b. initial values
		initialValues: {
			username: '',
			name: ''
		},
        // 3b. validation schema
		validationSchema: formSchema,
        // 3b. onSubmit callback
		onSubmit: (values, actions) => {
			fetch(signup ? '/users' : '/login', {
				method: 'POST',
				headers: {
					'content-type': 'application/json'
				},
				body: JSON.stringify(values)
			})
			.then(res => res.json())
			.then(data => {
				actions.resetForm()
				// 4c. pass result to updateUser to set state  
				updateUser(data)
            	// 4d. redirect to homepage if login is successful
				navigate('/')
			})
            
		}
	})
        
	return (
		<section>
			{signup ? (
				<form className="form" onSubmit={formik.handleSubmit}>
					<label>Name</label>
					<input value={formik.values.name} onChange={formik.handleChange} type="text" name='name' />
					<label>Username</label>
					<input value={formik.values.username} onChange={formik.handleChange} type="text" name='username' />
					<input type="submit" value="Sign Up" className="button" />
				</form>
			) : (
				<form className="form" onSubmit={formik.handleSubmit} >
					<label>Username</label>
					<input value={formik.values.username} onChange={formik.handleChange} type="text" name='username' />
					<input type="submit" value="Log In" className="button" />
				</form>
			)}
			<section>
				<p>{signup ? "Already have an account?" : "Not a member?"}</p>
				<button className="button" onClick={toggleSignup}>
					{signup ? "Login" : "Sign Up"}
				</button>
			</section>
		</section>
	);
}

export default Auth;
