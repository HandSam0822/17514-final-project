import React, { useEffect, useState } from 'react'

// import MessageArea from './MessageArea';
// import MessageRoomArea from './MessageRoomArea';
import {get, post} from "utils/sdk"
import "./message.scss"
import store from 'reducers/store'
// import { messageData } from './dummyData';

// UI source: https://codepen.io/Jackthomsonn/pen/jWyGvX
const Messages = () => {
    useEffect(()=> {      
      const id = store.getState().id; // 1 would be replaced to id in the future 
        post("messages/2", {user_id: 1}) // get all messages where <id>, where request user = user_id
        .then(response => {          
          let data = response.data;
          console.log(data.message);
          if (data.status !== 200) {
            console.log(data.error)
          } else {
            setMessages(data.message)
          }          
        })
              
    }, [])

    const [sent_text, set_sent_text] = useState("");
    const [messages, setMessages] = useState([]);

    const sendMessage = (e) => {
      e.preventDefault(); 
      post("send_message/2", {"message_text": sent_text, "user_id": 1}) 
      .then(resp=>{
        // console.log(resp.data.message)
        if (resp.data.status === 200) {          
          setMessages(prev => [...prev,
            resp.data.message
          ])
        }
        
        set_sent_text("");
      })
    }
  return (
      <>
      <div className='container'>
        <h1>Sent Message to React</h1>   
        <button onClick={()=>console.log(messages)}>click me</button>
        {
          React.Children.toArray(
            messages.map((m, index) => 
              <div className="chatbox__messages" key={index}>
                <div className="chatbox__messages__user-message">
                {/* if message at right if sent from user, else left */}
                {/*1 would later replaced by store id */}
                  <div className={ m.from_user_id.id === 2 ? "chatbox__messages__user-message--ind-message_l":"chatbox__messages__user-message--ind-message_r"}>
                    <p className="name">{m.from_user_id.username}</p>          
                    <p className="message">{m.message}</p>
                  </div>
                </div>
              </div>
            )
          )
        }

    <form onSubmit={(e)=>sendMessage(e)}>
      <input type="text" placeholder="Enter your message" 
      value={sent_text} name="message"
      onChange={(e)=>set_sent_text(e.target.value)} 
      autoComplete={"off"}
      />
    </form>
      </div>
      </>
    
  )
}

export default Messages;