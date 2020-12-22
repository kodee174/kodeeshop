import React, {useEffect, useState} from 'react';
import './HomePage.scss';
import {Grid, Container} from '@material-ui/core';

import humps from 'humps';
import HeaderPage from '../HeaderPage';
import FooterPage from '../FooterPage';
import TagList from '../../components/TagList';
import BannerBox from '../../components/BannerBox';
import TagService from '../../services/TagService';

interface TagState {
  id: number;
  name: string;
  slug: string;
  createdAt: string;
  updatedAt: string;
}

const HomePage = () => {
  const [tags, setTags] = useState<TagState[]>([]);

  useEffect(() => {
    TagService.getTags().then((data) => {
      setTags(data);
    });
  }, []);

  return (
    <div className="home-page">
      <Container maxWidth="lg">
        <HeaderPage />
        <Grid container item xs={12} spacing={3}>
          <Grid item xs={3}>
            <TagList title="Test Tags" tags={tags} />
          </Grid>
          <Grid item xs={6}>
            <BannerBox
              variant={1}
              image="https://cdn.shopify.com/s/files/1/0130/5041/3114/files/lay20_03_x1024.png?v=1551554827"
              title="Test banner 1"
              content="Test content 1"
            />
          </Grid>
          <Grid item xs={3}>
            <BannerBox
              variant={2}
              image="https://cdn.shopify.com/s/files/1/0130/5041/3114/files/lay20_04_x1024.png?v=1551554827"
              title="Test banner 2"
              content="Test Content 2"
            />
          </Grid>
        </Grid>
      </Container>
      <Container maxWidth={false}>
        <FooterPage />
      </Container>
    </div>
  );
};

export default HomePage;
