import React, { useState, useEffect } from 'react'
import axios from 'axios'
import ReactPaginate from 'react-paginate';
import './styles.css'
import Table from 'react-bootstrap/Table'
import 'bootstrap/dist/css/bootstrap.css';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Button from '@restart/ui/esm/Button';
import logo from "./logo.png";
function App() {
 const [postsPerPage,setPostPerPage] = useState(5);
 const [offset, setOffset] = useState(1);
 const [posts, setAllPosts] = useState([]);
 const [pageCount, setPageCount] = useState(0)
 const [query, setQuery] = useState("Search");

 
 const getAllPosts = async (query) => {

  const q = { query: query };
    const headers = { 
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    };
   const res = await axios.post(`http://127.0.0.1:8000/query` , q, { headers })

   const data = res.data.data;

   const slice = data.slice(offset - 1 , offset - 1 + postsPerPage)
    
   const postData = getPostData(slice)
   console.log(postData);
  
   setAllPosts(postData)
   setPageCount(Math.ceil(data.length / postsPerPage))
 }
 
 const handlePageClick = (event) => {
   const selectedPage = event.selected;
    setOffset(selectedPage + 1)
   
  
 };
 
 const handleSubmit = (event) => {
  document.getElementById("T").style.visibility = "visible";
  // document.getElementsByClassName("container").style.marginTop = "10px"; 
  event.preventDefault();
  getAllPosts(query)
}



  useEffect(() => {
    getAllPosts(query)
  }, [offset])
 

 
 return (
  <div className="container" style={{ marginTop: "100px"}}>
        {/* <div style={{ marginTop: "10px" }} className="ui container"> */}
        <center>
          
          <img  src={logo} />
       
        </center>
     <Container fluid  className="p-3">

          <Form onSubmit={handleSubmit}>
        <Row>
          <Col md>
          
          </Col>
          <Col  md>
               <Form.Control type="text" placeholder="Search" value={query}
          onChange={(e) => setQuery(e.target.value)}/>
          </Col>
          <Col>
          <Button class="btn btn-outline-primary" type="submit">
                <svg width="15px" height="15px">
                            <path d="M11.618 9.897l4.224 4.212c.092.09.1.23.02.312l-1.464 1.46c-.08.08-.222.072-.314-.02L9.868 11.66M6.486 10.9c-2.42 0-4.38-1.955-4.38-4.367 0-2.413 1.96-4.37 4.38-4.37s4.38 1.957 4.38 4.37c0 2.412-1.96 4.368-4.38 4.368m0-10.834C2.904.066 0 2.96 0 6.533 0 10.105 2.904 13 6.486 13s6.487-2.895 6.487-6.467c0-3.572-2.905-6.467-6.487-6.467 "></path>
                        </svg>
                       
                </Button>
          </Col>
         
        </Row>
      </Form>
      
      </Container>
      
     {/* <SearchBar onFormSubmit={getAllPosts()}> </SearchBar> */}
  <div id="T">

 
   
       {/* <Table  bordered hover variant="light" >  */}
     <table className="ui celled padded table">
      <thead className= "ui center aligned">
      {/* <thead className="thead-dark"> */}
      <tr>
          <th scope="col">Rank</th>
            <th scope="col">Source</th>
            <th scope="col">Acronym</th>
            <th scope="col">Dblp</th>
            <th scope="col">Conference</th>
        </tr>
      </thead>
    
      <tbody>
      {posts}

      </tbody>
  {/* </Table>  */}
       
  </table>
     
       
    <ReactPaginate 
       previousLabel={'<<'}
       nextLabel={'>>'}
       onPageChange={handlePageClick}
       containerClassName={'pagination justify-content-center'}
       pageClassName={'page-item'}
       pageCount={pageCount}
       pageLinkClassName={'page-link'}
       previousClassName={'page-item'}
       previousLinkClassName={'page-link'}
       nextClassName={'page-item'}
       nextLinkClassName={'page-link'}
       breakLinkClassName={'page-link'}
       breakClassName={'page-item'}
       activeClassName={'active'}
     
    />

  </div>
    </div>
 );
}
 
export default App;