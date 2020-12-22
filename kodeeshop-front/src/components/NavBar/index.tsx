import React from 'react';
import './NavBar.scss';

interface NavBarProps {
  items: {
    idItem: number;
    title: string;
    slug: string;
    current: boolean;
  }[];
}

const NavBar = (props: NavBarProps) => {
  const {items} = props;
  return (
    <div className="navbar">
      <ul className="navbar__list">
        {items.map((item) => {
          return item.current ? (
            <li key={item.idItem} className="navbar__list--current">
              <a href={item.slug}>{item.title}</a>
            </li>
          ) : (
            <li key={item.idItem}>
              <a href={item.slug}>{item.title}</a>
            </li>
          );
        })}
      </ul>
      <ul className="navbar__list navbar__list--right">
        <li className="account">
          <a href="/login">Đăng nhập</a>
        </li>
        <li>hoặc</li>
        <li className="account">
          <a href="/register">Đăng ký</a>
        </li>
      </ul>
    </div>
  );
};

export default NavBar;
