import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import G6 from '@antv/g6';

import dataset from './data/dataset'
import useWindowSize from './hooks/useWindowSize';

const App = () => {
  const ref = React.useRef(null);
  const { screenWidth, screenHeight } = useWindowSize();

  useEffect(() => {
    if (!screenWidth || !screenHeight) {
      return;
    }
    const graph = new G6.Graph({
      container: (ReactDOM.findDOMNode(ref.current) as HTMLElement) ,
      width: screenWidth,
      height: screenHeight,
      modes: {
        default: ['drag-canvas', 'zoom-canvas'],
      },
      layout: {
        type: 'dagre',
        direction: 'TB',
        nodesep: 50,
        ranksep: 10,
      },
      defaultNode: {
        type: 'node',
        labelCfg: {
          style: {
            fill: '#000000A6',
            fontSize: 16,
          },
        },
        style: {
          stroke: '#72CC4A',
          width: 150,
        },
      },
      defaultEdge: {
        type: 'polyline',
      },
    });
    graph.data(dataset as any);
    graph.render();
  }, [screenWidth, screenHeight]);

  return <div ref={ref}></div>;
}

export default App
