import React, { useState, useEffect } from "react";
import axios from "axios";

function Imageupload(){
    const [picture, setPicture] = useState('');
    const [name, setName] = useState('');
    function handleImage(e){
      console.log(e.target.files)
      setPicture(e.target.files[0])
    }
    function handleApi(){
      const formData = new FormData()
      formData.append('picture', picture)
      axios.post('http://localhost:8000/api/n_profiles/', formData).then((res) => {
        const extractedMake = res.data.make_name;
        setName(extractedMake);
      }).catch((error) => console.error('Error fetching data:', error));
    }


    return(
      <div>
        <input type="file" name='file' onChange ={handleImage}/>
        <button onClick= {handleApi}>Submit</button>
        <div>{name}</div>
      </div>

    
    )
}

export default Imageupload;
