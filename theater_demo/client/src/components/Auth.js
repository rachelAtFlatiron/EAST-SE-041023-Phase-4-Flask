import { useNavigate } from 'react-router-dom'
import { useState } from "react";
import { useFormik } from 'formik'
import * as yup from 'yup'

function Auth({ updateUser }) {
	const [signup, setSignup] = useState(true);
    const navigate = useNavigate()
	const toggleSignup = () => setSignup((prev) => !prev);

    // 3a. create a validations schema using yup
    // 3b. create a formik instance containing...
        // 3b. initial values
        // 3b. validation schema
        // 3b. onSubmit callback

                // 4c. pass result to updateUser to set state  
                // 4d. redirect to homepage if login is successful
    
	return (
		<section>
			{signup ? (
				<form className="form" >
					<label>Name</label>
					<input type="text" name='name' />
					<label>Username</label>
					<input type="text" name='username' />
					<input type="submit" value="Sign Up" className="button" />
				</form>
			) : (
				<form className="form" >
					<label>Username</label>
					<input type="text" name='username' />
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
