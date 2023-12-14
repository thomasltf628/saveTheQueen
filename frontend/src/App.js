import React, { useState, useEffect } from "react";
import Imageupload from "./components/FileUpload";
import './App.css'
import { Navbar } from "./components/Navbar/Navbar";

const App = () => {
  return (
    <div >
      <Navbar/>
      <Imageupload/>
    </div> 

  )
}
export default App