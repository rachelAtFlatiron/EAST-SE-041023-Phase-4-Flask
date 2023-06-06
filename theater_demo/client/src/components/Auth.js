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
        name: yup.string(), // 🛑 not required due to login form
        username: yup.string().required("Please enter a username")
    })
    const formik = useFormik({
        initialValues: {
            username: '',
            name: ''
        },
        validationSchema: formSchema,
        // 🛑 pass in actions to have access to reset form
        onSubmit: (values, actions) => {
            // 🛑 need to conditionally render between /users and /login due to forms
            // 🛑 may write /login later
            fetch(signup ? '/users' : '/login', {
                method: 'POST',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => res.json())
            .then(data => {
                // 🛑 reset form
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
					<input type="text" name='name' value={formik.values.name} onChange={formik.handleChange} />
					<label>Username</label>
					<input type="text" name='username' value={formik.values.username} onChange={formik.handleChange}  />
					<input type="submit" value="Sign Up" className="button" />
				</form>
			) : (
				<form className="form" onSubmit={formik.handleSubmit}>
					<label>Username</label>
					<input type="text" name='username' value={formik.values.username} onChange={formik.handleChange}  />
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
