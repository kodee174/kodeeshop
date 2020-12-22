import React from 'react';
import './ProductQuickView.scss';
import {Grid, Dialog, DialogTitle, DialogContent} from '@material-ui/core';
import Icon from '../Icon';

type Product = {
  idProduct: number;
  image: string;
  title: string;
  primaryPrice: number;
  salePrice: number;
};

type Cart = {
  totalItem: number;
  totalPrice: number;
};

type CustomProduct = {
  idProduct: number;
  image: string;
  title: string;
  slug: string;
  price: number;
};

interface ProductQuickViewProps {
  show: boolean;
  handleClose: () => void;
  message: string;
  product: Product;
  cart: Cart;
  customTitle: string;
  customProducts: CustomProduct[];
}

const defaultProps = {
  show: false,
};

const ProductQuickView = (props: ProductQuickViewProps) => {
  const {show, handleClose, message, product, cart, customTitle, customProducts} = props;
  return (
    <Dialog open={show}>
      <DialogTitle>
        <div className="product-quick-view__message">
          <Icon icon={['fas', 'check']} />
          <span>{message}</span>
        </div>
        <div className="product-quick-view__close" onClick={() => handleClose()}>
          <Icon icon={['fas', 'times']} />
        </div>
      </DialogTitle>
      <DialogContent>
        <div className="product-quick-view">
          <Grid container spacing={3}>
            <Grid item xs={6}>
              <div className="product-quick-view__product">
                <img className="product-quick-view__product__image" src={product.image} alt={product.title} />
                <div className="product-quick-view__product__title">{product.title}</div>
                <div className="product-quick-view__product__price product-quick-view__product__price--primary">
                  {product.primaryPrice}₫
                </div>
                <div className="product-quick-view__product__price product-quick-view__product__price--sale">
                  {product.salePrice}₫
                </div>
              </div>
            </Grid>
            <Grid item xs={6}>
              <div className="product-quick-view__cart">
                <div className="product-quick-view__cart__count">Có {cart.totalItem} trong giỏ hàng</div>
                <div className="product-quick-view__cart__price">
                  Tổng: <span>{cart.totalPrice}₫</span>
                </div>
                <div className="product-quick-view__cart__action">
                  <a href="/checkout">
                    <button className="product-quick-view__cart__action__checkout">
                      <Icon icon={['fas', 'shopping-bag']} />
                      <span>Thanh toán</span>
                    </button>
                  </a>
                  <button className="product-quick-view__cart__action__continue-shopping" onClick={() => handleClose()}>
                    <Icon icon={['fas', 'shopping-cart']} />
                    <span>Tiếp tục mua hàng</span>
                  </button>
                </div>
              </div>
            </Grid>
            <Grid item xs={12}>
              <div className="product-quick-view__custom-title">{customTitle}</div>
            </Grid>
            {customProducts.map((customProduct) => {
              return (
                <Grid key={`customProduct-${customProduct.idProduct}`} item xs={3}>
                  <div className="product-quick-view__custom-product">
                    <a href={customProduct.slug}>
                      <img
                        className="product-quick-view__custom-product__image"
                        src={customProduct.image}
                        alt={customProduct.title}
                      />
                      <div className="product-quick-view__custom-product__title">{customProduct.title}</div>
                      <div className="product-quick-view__custom-product__price">{customProduct.price}₫</div>
                    </a>
                  </div>
                </Grid>
              );
            })}
          </Grid>
        </div>
      </DialogContent>
    </Dialog>
  );
};

ProductQuickView.defaultProps = defaultProps;

export default ProductQuickView;
