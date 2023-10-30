import React, { useState } from "react";
import axios from "axios";

function Imageupload(){
    const [picture, setPicture] = useState('')
    function handleImage(e){
      console.log(e.target.files)
      setPicture(e.target.files[0])
    }
    function handleApi(){
      const formData = new FormData()
      formData.append('name', "Default")
      formData.append('bio','Default')
      formData.append('picture', picture)
      axios.post('http://localhost:8000/api/n_profiles/', formData).then((res) => {
        console.log(res)

      })
    }


    return(
      <div>
        <input type="file" name='file' onChange ={handleImage}/>
        <button onClick= {handleApi}>Submit</button>
      </div>

    
    )
}

export default Imageupload;