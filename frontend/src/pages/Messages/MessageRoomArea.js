import React from 'react'
// import "./message.css"

/**
 * Get all user that has chat history with user, fetch that number of room
 * @returns 
 */
const MessageRoomArea = (props) => {
  // const data = props.data
  let data = ['Kim', 'Elain'];

  const chatterDiv = data.map((ele) => 
        <div key={ele} className="" style={{borderStyle: "dotted", padding: "0.5rem", margin: "0.5rem"}}>            
           <div>Chat with {ele}</div>
        </div>
    )
  return (
    <div className='message-room-area'>    
        {chatterDiv}
        
    </div>
  )
}

export default MessageRoomArea