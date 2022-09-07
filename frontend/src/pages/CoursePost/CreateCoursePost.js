import React, { useState } from 'react'
import { Button, Form } from 'react-bootstrap/';
import { redirect } from "utils/sdk"
import { createPost } from 'utils/crud';
const CreateCoursePost = () => {    
    const [postContent, setPostContent] = useState({
        "course_number":"",  
        "course_post_title": "",
        "course_post_text": "",              
    });

    const handleChange = (e) => {
        const name = e.target.id;
        const value = e.target.value;
        setPostContent(prevValue => {
            return {
                ...prevValue,
                [name]: value
            }
        })
        console.log(postContent)
    }

    return (
        <>
            <br></br>
            <Form style={{ marginLeft: "400px" }}>
                <Form.Group className="mb-3" controlId="course_number">
                    <Form.Label>Course Number</Form.Label>
                    <Form.Control 
                    onChange={(e) => handleChange(e)}                     
                    autoFocus = "on"
                    required="required"
                    pattern='[0-9]*'
                    autoComplete='off'
                    onInput={(e)=>handleChange(e)}
                    value = {postContent.course_number}
                    placeholder="Enter course number" />
                    <Form.Text className="text-muted">
                        Please enter in 5 digit format such as 18613, 17637 <br></br>
                        Any other format is invalid. Ex: 17-673, 12A59, 99999, etc
                    </Form.Text>
                </Form.Group>

                <Form.Group className="mb-3" controlId="course_post_title">
                    <Form.Label>Title</Form.Label>
                    <Form.Control autoComplete='off' 
                    onChange={(e) => handleChange(e)} type="text"/>                   
                </Form.Group>

                <Form.Group className="mb-3" controlId="course_post_text">
                    <Form.Label>Post</Form.Label>
                    <Form.Control  onChange={(e) => handleChange(e)} as="textarea" rows={4} placeholder="What's in your mind abt this course" />
                </Form.Group>


                <Form.Group className="mb-3" controlId="formBasicCheckbox">
                    <Form.Check type="checkbox" label="Anonymous" />
                </Form.Group>
                <Button className="m-1" variant="outline-primary" onClick={() => createPost("course_post", postContent)}>
                    Post
                </Button>
                <Button className="m-1" variant="outline-secondary" onClick={() => redirect("/coursePost")}>
                    Cencel
                </Button>
            </Form>

        </>
    )
}

export default CreateCoursePost