import React from 'react';
import './Header.scss';
import {Grid} from '@material-ui/core';
import Icon from '../Icon';
import NavBar from '../NavBar';

interface HeaderProps {
  items: {
    idItem: number;
    title: string;
    slug: string;
    current: boolean;
  }[];
}

const Header = (props: HeaderProps) => {
  const {items} = props;
  return (
    <header>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <NavBar items={items} />
        </Grid>
        <Grid item xs={12}>
          <div className="header">
            <Grid item xs={3}>
              <div className="header__logo">
                <img
                  src="https://cdn.shopify.com/s/files/1/0130/5041/3114/files/Logo_145x.png?v=1551529109"
                  alt="Kodeeshop"
                />
              </div>
            </Grid>
            <Grid item xs={5}>
              <div className="header__search">
                <form action="#search">
                  <input type="text" className="header__search__form-input" placeholder="Tìm kiếm sản phẩm,..." />
                  <button className="header__search__button">
                    <Icon icon={['fas', 'search']} />
                  </button>
                </form>
              </div>
            </Grid>
            <Grid item xs={2}>
              <div className="header__info">
                <span className="header__info__phone">Call: +84 942 480 496</span>
                <span className="header__info__time">From 8:00 to 21:00 (Mon-Sun)</span>
              </div>
            </Grid>
            <Grid item xs={1}>
              <div className="header__favourite">
                <a href="/favourite">
                  <Icon icon={['fas', 'heart']} size="2x" />
                  <span>Yêu thích</span>
                </a>
              </div>
            </Grid>
            <Grid item xs={1}>
              <div className="header__cart">
                <a href="/cart">
                  <Icon icon={['fas', 'shopping-cart']} size="2x" />
                  <span>Giỏ hàng</span>
                </a>
              </div>
            </Grid>
          </div>
        </Grid>
      </Grid>
    </header>
  );
};

export default Header;
