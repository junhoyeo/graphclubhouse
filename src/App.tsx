import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import G6 from '@antv/g6';

import dataset from './data/dataset';
import useWindowSize from './hooks/useWindowSize';

const App = () => {
  const ref = React.useRef(null);
  const { screenWidth, screenHeight } = useWindowSize();

  useEffect(() => {
    if (!screenWidth || !screenHeight) {
      return;
    }
    const graph = new G6.Graph({
      container: ReactDOM.findDOMNode(ref.current) as HTMLElement,
      width: screenWidth,
      height: screenHeight,
      modes: {
        default: ['drag-canvas', 'zoom-canvas'],
      },
      layout: {
        type: 'dagre',
        direction: 'TB',
        nodesep: 50,
        ranksep: 15,
      },
      defaultNode: {
        type: 'node',
        size: 36,
        labelCfg: {
          style: {
            fill: '#262525',
            fontSize: 16,
          },
        },
        style: {
          fill: '#d9d9d9',
          stroke: '#c5c5c5',
        },
      },
      defaultEdge: {
        type: 'polyline',
        style: {
          stroke: '#5a543e50',
        },
      },
    });
    graph.data(dataset as any);
    graph.render();
  }, [screenWidth, screenHeight]);

  return <div ref={ref} style={{ backgroundColor: '#eeecdd' }}></div>;
};

export default App;
