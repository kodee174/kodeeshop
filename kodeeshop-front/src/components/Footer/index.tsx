import React from 'react';
import './Footer.scss';
import {Grid, Container} from '@material-ui/core';
import Icon from '../Icon';

interface FooterProps {
  collections: {
    idCollection: number;
    name: string;
    slug: string;
  }[];
}

const Footer = (props: FooterProps) => {
  const {collections} = props;
  return (
    <footer>
      <div className="footer-top">
        <Container maxWidth="lg">
          <Grid container spacing={3}>
            <Grid item xs={4}>
              <h4 className="footer-top__title">BE IN TOUCH WITH US:</h4>
            </Grid>
            <Grid item xs={4}>
              <h4 className="footer-top__subcrible">Test</h4>
            </Grid>
            <Grid item xs={4}>
              <ul className="footer-top__network">
                <li>
                  <a href="#facebook">
                    <Icon icon={['fab', 'facebook']} size="2x" />
                  </a>
                </li>
                <li>
                  <a href="#twitter">
                    <Icon icon={['fab', 'twitter']} size="2x" />
                  </a>
                </li>
                <li>
                  <a href="#google">
                    <Icon icon={['fab', 'google']} size="2x" />
                  </a>
                </li>
              </ul>
            </Grid>
          </Grid>
        </Container>
      </div>
      <div className="footer">
        <Container maxWidth="lg">
          <Grid container item xs={12} spacing={3}>
            <Grid item xs={3}>
              <h4 className="footer__title">Collection</h4>
              <ul className="footer__list">
                {collections.map((collection) => {
                  return (
                    <li key={`collection-${collection.idCollection}`}>
                      <a href={collection.slug}>{collection.name}</a>
                    </li>
                  );
                })}
              </ul>
            </Grid>
            <Grid item xs={3}>
              <div className="footer__title">Buy With Us</div>
              <ul className="footer__list">
                <li>
                  <a href="#">About Us</a>
                </li>
                <li>
                  <a href="#">Services</a>
                </li>
                <li>
                  <a href="#">Contact Us</a>
                </li>
                <li>
                  <a href="#">FAQs</a>
                </li>
              </ul>
            </Grid>
            <Grid item xs={3}>
              <div className="footer__title">About</div>
              <div className="footer__about">
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
                commodo consequat tempor incididunt.
              </div>
            </Grid>
            <Grid item xs={3}>
              <div className="footer__title">Contact Us</div>
              <div className="footer__contact">
                <p>
                  <span>ADDRESS:</span>
                  7895 Piermont Dr NE Albuquerque, NM 198866, United States of America
                </p>
                <p>
                  <span>PHONE:</span>
                  +566 4774 9930; +566 4774 9940
                </p>
                <p>
                  <span>HOURS:</span>
                  all week from 9 am to 9 pm
                </p>
                <p>
                  <span>E-MAIL:</span>
                  info@mydomain.com
                </p>
              </div>
            </Grid>
          </Grid>
        </Container>
      </div>
    </footer>
  );
};

export default Footer;
