Client side code for MOE. 

Install MOE with docker and call it using python REST interface   

See https://github.com/Yelp/MOE/issues/461

[MOE](https://github.com/Yelp/MOE) A global, black box optimization engine for real world metric optimization.


## Install
`pip install clientMOE`

## Eaxmples
* python [start_moe_example.py](https://github.com/mulyoved/clientMOE/blob/master/start_moe_example.py) 
* jupyter notebook [example.ipynb](https://github.com/mulyoved/clientMOE/blob/master/jupyter-examples/example.ipynb) 


# Development
## Publish PyPi package
`python setup.py sdist register upload -r pypitest`
`python setup.py sdist register upload -r pypi`

