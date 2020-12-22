import React, {useEffect, useState} from 'react';
// import './FooterPage.scss';

import Footer from '../../components/Footer';
import CollectionService from '../../services/CollectionService';

interface CollectionState {
  idCollection: number;
  name: string;
  slug: string;
}

const FooterPage = () => {
  const [collections, setColections] = useState<CollectionState[]>([]);

  useEffect(() => {
    CollectionService.getCollections().then((data) => {
      setColections(data);
    });
  }, []);

  return (
    <div className="footer-page">
      <Footer collections={collections} />
    </div>
  );
};

export default FooterPage;
