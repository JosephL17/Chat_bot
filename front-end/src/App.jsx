import { useState } from 'react'
import './App.css'
import ChatComponent from './components/ChatComponent'

function App() {
  

  return (
    <div className="flex flex-col justify-center items-center h-screen bg-slate-400 overflow-auto">
      <div className="bg-white p-6 rounded-lg shadow-lg max-w-screen-sm overflow-auto">
        <h1>Chatbot</h1>
        <ChatComponent />
      </div>
    </div>
  );
}

export default App
