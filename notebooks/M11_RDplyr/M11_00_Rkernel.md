# How to Create an R Kernel for Jupyter Lab


```yaml
Course:   DS 5100
Module:   11 R Programming II
Topc:     R Kernel
Author:   R.C. Alvarado
Date:     8 April 2024
```

**Motivation**

You want to run R in a Jupyter notebook. This means having available an R kernel in the list of kernels you see in the Launcher window (in Jupyter Lab).


**1. Create and activate an R environment with Conda**

From the command line in Rivanna, create and activate an R environment. 

First, create one with the essentials and base packages for R using this command:

```bash
conda create -n r_env r-essentials r-base
```

Then activate the environment with this command:

```bash
conda activate r_env
```

You are now in an environment that runs R.


**2. Run the R shell**

Now, run R from the command line like so:

```bash
R
```

**3. Register the kernel**

Once in the R interactive shell, register the kernel with the following commands:  

```r
install.packages("IRkernel") # Not really needed since included in r-essentials
IRkernel::installspec(name = 'r_env', displayname = 'R Environment')
quit()
```

**4. Deactivate the environment**

Once you are done with this, you can deactivate the environment like so:

```bash
conda deactivate
```

**5. Run Jupyter Lab**

Now start Jupyter Lab from the [OpenOnDemand webpage](https://ood.hpc.virginia.edu/pun/sys/dashboard). 

If you already have a session running, close it down and restart it.

You should see a kernel tile like the following in the launcher window:

![](./images/r-kernel.png)


**6. Going Forward**

If everything worked, you can close down the command line terminal and work in Jupyter Lab.

Note that you can add more packages to your R environment by issuing the command from within the R environment:

```bash
conda install -c r <r-package>
```

`<r-package>` can be anything from the following list:

- https://repo.anaconda.com/pkgs/r/

Or, if you are not in the R environment, you can specify the target environment with the argument `-n`:

```bash
conda install -n r_env -c r <r-package>
```