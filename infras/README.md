
[![Build Status](https://dev.azure.com/rabahbrahami/myproject-teoschool/_apis/build/status/myproject-teoschool-CI?branchName=main)](https://dev.azure.com/rabahbrahami/myproject-teoschool/_build/latest?definitionId=11&branchName=main)

After deploying this infrastructure you'll have to do one step to synchronise your cluster AKS and git repository:
- take the key SSH returned at the end of the deployment
- add it to the deploy key in the setting of rest git "setting > deploy key > add key > Allow write access > Add key"
