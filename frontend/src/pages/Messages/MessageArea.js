import React from 'react'
// import "./message.css"
const MessageArea = (props) => {
    const messages =  props.data;
    const listItems = messages.map((message) => 
        <div key={message.id} className="" style={{borderStyle: "dotted", padding: "0.5rem", margin: "0.5rem"}}>
            <div>Message id: {message.id}</div>
            <div>Message: {message.message}</div>
            <div>Create time: {message.create_time}</div>
            <div>From user id: {message.from_user_id}</div>
            <div>To user id: {message.to_user_id}</div>
        </div>
    )
    
  return (
    <div className='message-area'>
        {listItems}
    </div>
  )
}

export default MessageArea