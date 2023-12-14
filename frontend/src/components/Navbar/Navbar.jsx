import React from 'react'
import './Navbar.css'
import logo from '../Assets/priceimg.png'
import iicon from '../Assets/letter.png'
import loginlogo from '../Assets/enter.png'

export const Navbar = () => {
  return (
    <div className='navbar'>
    <div className="nav-logo">
      <img src={logo} alt='' />
        <p>Price Prediction</p>
    </div>
    <ul className='nav-menu'>
        <li>Home</li>
        <li>Result</li>
        <li>About</li>
      </ul>
      <div className='nav-login'>
      <button>Login</button>
        <img src={loginlogo} alt="" />
      </div>
</div>
  )
}
