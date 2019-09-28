Example high resolution image source: http://highresolution.photography/it-s-hard-to-believe-your-eyes/


Considerations
===

Core algorithm
- Kmeans clustering might produce better results, in particular if an image is not dominated by one colour but by a few
- Distance from swatch mechanism was not defined in test criteria
- Multiprocessing?

Product/Customer process
- What if the image is not dominated by a single colour (see above)?
- What is the correct way to determine distance of one colour from another?
- How much latency can the system endure before it impacts the fulfilment partner?
- While it almost certainly is something we can do in house, is it something we should do in house? In this example I'd almost certainly assume so but for other things it might be a cheaper solution exists by outside the company
