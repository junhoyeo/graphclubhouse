import graph from './graph.json'

const nodes = graph.map(({ user_id, ...props }) => ({
  id: user_id.toString(),
  label: props.name,
  x: 0,
  y: 0,
  // ...props,
}))

const edges = graph.flatMap((node) => {
  const currentNode = {
    source: node.referrer !== null ? node.referrer.toString() : null,
    target: node.user_id !== null ? node.user_id.toString(): null,
  }
  if (!!currentNode.source
    && nodes.find(v => v.id === currentNode.source)
    && nodes.find(v => v.id === currentNode.target)) {
    return [currentNode]
  }
  return []
})

const dataset = {
  nodes,
  edges
}

export default dataset
