Requirements
> pip3 install pillow flask


# Considerations

### Core algorithm
- Kmeans clustering might produce better results, in particular if an image is not dominated by one colour but by a few
- Multiprocessing? I would expect we can more rapidly find the most common pixel but splitting the image up; my attempts to test this were why the swatch_file() function was created

### Product/Customer process
- What if the image is not dominated by a single colour (see above)?
- What is the correct way to determine distance of one colour from another?
- How much latency can the system endure before it impacts the fulfilment partner?
- While it almost certainly is something we can do in house, is it something we should do in house? In this example I'd almost certainly assume so but for other things it might be a cheaper solution exists by outside the company

### Scale
Each separate request is completely independent with no shared state so in theory it should be relatively easy to scale. My main concern would be how efficient the methodology is and if Pillow is the best library for this sort of image manipulation.

### Efficiency
As mentioned in scale above I am not sure how efficient the Pillow library is. Worse still, if an image is composed of multiple dominant colours this method may be completely ineffective rendering the efficiency moot. If we find the same image is being queries multiple times it would be trivial to put an LRU cache in place using the standard library decorator.

### Resilience - External
As it stands this service is wholly and completely vulnerable to DOS attacks. The first step would be to put a basic auth in place and secondly a rate limiter. If an attack started as a relatively simple attack we could use caching to prevent repeatedly running the same calculations while at the same time adding in a delay when using the cache to make the attacker think we have not responded to them.

### Resilience - Internal
While not 100% code coverage the core functionality of the system is tested. The system is written in a manner hopefully enabling the quick swapping out of components. Functionality was simple enough classes were not needed for this.

### Alerting/Monitoring - Accuracy
swatcher.py lines 83 and 95 are ready for a logging function to be put in place to alert us to when images are not matching closely enough to the swatch. We could look to add logging in place to for all outputs and enable fulfilment partners to submit feedback when a swatch was not correct, essentially giving us extra sets of eyes on the system. 

### Alerting/Monitoring - Stability
Currently there is nothing in the system to enable monitoring of system health. It would be easy to include a timer (possibly at a separate endpoint) to allow us to monitor the speed of the system. I would expect a lot of the details in this section to be dictated in part by the choice of hosting method.
