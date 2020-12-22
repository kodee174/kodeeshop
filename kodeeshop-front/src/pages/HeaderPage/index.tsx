import React from 'react';
// import './Header.scss';

import Header from '../../components/Header';

const HeaderPage = () => {
  return (
    <div className="header-page">
      <Header
        items={[
          {idItem: 1, title: 'Trang chủ', slug: '#home', current: true},
          {idItem: 2, title: 'Sản phẩm', slug: 'products', current: false},
          {idItem: 3, title: 'Chủ đề', slug: 'tags', current: false},
          {idItem: 4, title: 'Giỏ hàng', slug: 'carts', current: false},
          {idItem: 5, title: 'Liên hệ', slug: 'contact', current: false},
        ]}
      />
    </div>
  );
};

export default HeaderPage;
