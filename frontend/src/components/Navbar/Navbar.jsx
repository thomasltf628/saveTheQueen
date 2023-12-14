import React, { useState } from 'react'
import './Navbar.css'
import logo from '../Assets/priceimg.png'
import iicon from '../Assets/letter.png'
import loginlogo from '../Assets/enter.png'

export const Navbar = () => {
  const [menu,setMenu]=useState("home")
  return (
    <div className='navbar'>
    <div className="nav-logo">
      <img src={logo} alt='' />
        <p>Price Prediction</p>
    </div>
    <ul className='nav-menu'>
        <li onClick={()=>{setMenu("home")}}>Home{menu==="home"?<hr/>:<></>}</li>
        <li onClick={()=>{setMenu("result")}}>Result{menu==="result"?<hr/>:<></>}</li>
        <li onClick={()=>{setMenu("about")}}>About{menu==="about"?<hr/>:<></>}</li>
      </ul>
      <div className='nav-login'>
      <button>Login</button>
        <img src={loginlogo} alt="" />
      </div>
</div>
  )
}
