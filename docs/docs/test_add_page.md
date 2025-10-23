## test_add_page

md 文件里推荐相对路径，如果需要增加锚点的话，就使用 # 号去处理

ipynb 文件里推荐使用相对路径，但是不能包含文件名（但是因为ipynb 文件本身也会被解析为目录，所以需要额外增加`../`）

## test link

- [url link without latest](/reference/bridgic-core/bridgic/core/agentic/)
- [url link](/latest/reference/bridgic-core/bridgic/core/agentic/)
- [relative file path✅](./reference/bridgic-core/bridgic/core/agentic/index.md)
- [relative file path with anchor✅](./reference/bridgic-core/bridgic/core/agentic/index.md#bridgic.core.agentic.ConcurrentAutomaV5.run)
- [absolute file path](/docs/docs/reference/bridgic-core/bridgic/core/agentic/index.md)
- [absolute file path with anchor](/docs/docs/reference/bridgic-core/bridgic/core/agentic/index.md#bridgic.core.agentic.ConcurrentAutomaV5.run)

```md

- [url link without latest](/reference/bridgic-core/bridgic/core/agentic/)
- [url link](/latest/reference/bridgic-core/bridgic/core/agentic/)
- [relative file path✅](./reference/bridgic-core/bridgic/core/agentic/index.md)
- [relative file path with anchor✅](./reference/bridgic-core/bridgic/core/agentic/index.md#bridgic.core.agentic.ConcurrentAutomaV5.run)
- [absolute file path](/docs/docs/reference/bridgic-core/bridgic/core/agentic/index.md)
- [absolute file path with anchor](/docs/docs/reference/bridgic-core/bridgic/core/agentic/index.md#bridgic.core.agentic.ConcurrentAutomaV5.run)

```