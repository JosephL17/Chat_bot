import React, { useState } from 'react';
import axios from 'axios';


// const ChatComponent = () => {
//   const [message, setMessage] = useState('');
//   const [response, setResponse] = useState('');

//   const handleSendMessage = async () => {
//     try {
//       const result = await axios.post('/http://127.0.0.1:5000', { message });
//       setResponse(result.data.response);
//     } catch (error) {
//       console.error("Error sending message:", error);
//     }
//   };

//   return (
//     <div>
//       <textarea
//         value={message}
//         onChange={(e) => setMessage(e.target.value)}
//         rows="4"
//         cols="50"
//       />
//       <button onClick={handleSendMessage}>Send</button>
//       <div>
//         <strong>Response:</strong>
//         <p>{response}</p>
//       </div>
//     </div>
//   );
// };

// export default ChatComponent;

const ChatComponent = () => {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');
    const [context, setContext] = useState('');
  
    const handleSendMessage = async () => {
      try {
        const result = await axios.post('http://127.0.0.1:5000/api/chat', { 
          message, 
          context 
        });
        setMessage('')
        setResponse(result.data.response);
        setContext(result.data.context);
      } catch (error) {
        console.error("Error sending message:", error);
      }
    };
  
    return (
      <div>
        <textarea className=' rounded-lg overflow-auto'
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          rows="4"
          cols="50"
          placeholder='message ChatBot'
        />
        <button className='rounded-md font-bold py-2 px-4 hover:bg-stone-900 hover:text-white' onClick={handleSendMessage}>Send</button>
        <div>
          <strong>Response:</strong>
          <p className='overflow-auto'>{response}</p>
        </div>
      </div>
    );
  };
  
  export default ChatComponent;