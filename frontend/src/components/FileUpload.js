import React, { useState, useEffect } from "react";
import axios from "axios";
import DataTable from "./DataTable";

function Imageupload(){
    const [picture, setPicture] = useState('');
    const [jsonData, setJsonData] = useState(null);
    const [modelName, setModelName] = useState('');
    function handleImage(e){
      console.log(e.target.files)
      setPicture(e.target.files[0])
    }
    async function handleApi(){
      const formData = new FormData()
      formData.append('picture', picture)
      await axios.post('http://localhost:8000/api/n_profiles/', formData).then((res) => {
        console.log(res.data) 
        const extractedModel = res.data.model_name;
        setModelName(res.data.make_name + " " + res.data.model_name)
        return axios.get(`http://localhost:8000/api/cars/?model=${extractedModel}`);
      }).then(
        response => typeof response.data ==='string'? JSON.parse(response.data): response.data).then(data => { 
        setJsonData(data);
      }).catch((error) => console.error('Error fetching data:', error));
    }


    return(
      <div>
        <input type="file" name='file' onChange ={handleImage}/>
        <button onClick= {handleApi}>Submit</button>

        {modelName && <h3>It is a {modelName}</h3>}
        <DataTable  jsonData={jsonData}/>
      </div>

    
    )
}

export default Imageupload;
