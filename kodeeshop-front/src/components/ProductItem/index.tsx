import React from 'react';
import './ProductItem.scss';
import Icon from '../Icon';

interface ProductItemProps {
  label: string;
  image: string;
  title: string;
  slug: string;
  primaryPrice: number;
  salePrice: number;
  handleAddToCart: () => void;
  back?: boolean;
  next?: boolean;
}

const defaultProps = {
  back: false,
  next: false,
};

const ProductItem = (props: ProductItemProps) => {
  const {back, label, image, title, slug, salePrice, primaryPrice, handleAddToCart, next} = props;
  return (
    <div className="product-item">
      {back ? (
        <div className="product-item__more product-item__more--back">
          <Icon icon={['fas', 'angle-left']} />
        </div>
      ) : null}
      {label === 'new' ? <div className="product-item__label product-item__label--new">New</div> : null}
      {label === 'hot' ? <div className="product-item__label product-item__label--hot">Hot</div> : null}
      {label === 'sale' ? <div className="product-item__label product-item__label--sale">Sale</div> : null}
      <div className="product-item__favourite">
        <Icon icon={['fas', 'heart']} />
      </div>
      <img className="product-item__image" src={image} alt={title} />
      <div className="product-item__info">
        <h3>
          <a className="product-item__info__title" href={slug}>
            {title}
          </a>
        </h3>
        <div className="product-item__info__price product-item__info__price--sale">{salePrice}₫</div>
        <div className="product-item__info__price product-item__info__price--primary">{primaryPrice}₫</div>
      </div>
      <button className="product-item__cart" onClick={() => handleAddToCart()}>
        <Icon icon={['fas', 'shopping-cart']} />
        <span>Thêm vào giỏ hàng</span>
      </button>
      {next ? (
        <div className="product-item__more product-item__more--next">
          <Icon icon={['fas', 'angle-right']} />
        </div>
      ) : null}
    </div>
  );
};

ProductItem.defaultProps = defaultProps;

export default ProductItem;
