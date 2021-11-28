import React, { useState } from 'react';
import { useEffect } from 'react';
import ReactDOM from 'react-dom';
import ConfAPI from "./apis/flask-conf";
import axios from 'axios';
import "./styles.css";
import App from './App'
// function App(){
//   const [posts,setPosts] = useState([]);
//   const [loading,setLoading] = useState(false);
//   const [currentPage,setCurrentPage] = useState(1);
//   const [postsPerPage,setPostPerPage] = useState(5);

 
//   const fetchPosts = async ()=>{
//         const res = await ConfAPI.post("/query", {
//           query: "Machine",
//         });
        
//         console.log(res.data);
//         console.log("abcd");
//         setPosts(res.data);
//         setLoading(false);

      
        
//   };


//   fetchPosts();


//   console.log(posts);
//   console.log("abcd");
//   return (
//     <h1>a</h1>
//   );
// }


// const rootElement = document.getElementById('root');
// ReactDOM.render(<App />, rootElement);

ReactDOM.render(
  <React.StrictMode>
   <App />
  </React.StrictMode>,
  document.getElementById('root')

);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
