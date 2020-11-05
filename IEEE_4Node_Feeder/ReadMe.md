**UPDATE**
(01/26/2020)

File is cmopleted and ready for testing. Download the following files from this repo and make sure they are in the same directory:

- May_29_IEEE_Node_4_Feeder.glm
- converted0.csv

**DO NOT** use excel to open CSV files. It changes the timestamp column format. Open it with any other text editor. I recommend **NotePad++** or **sublime text**

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

This is file is to test Feeder 4 capeabilities of upholding different loads. Also, this file is edited from the original file in Gridlab-d Samples folder"IEEE_Feeder_4_node_with_Loads".
As far as of today, (12/26/2019)I have finished two attempts as follows:

	a) attached only one load to the 4th node and measured the power at node 3 (node three after the xformer)
	b) attached the same load in previous attempt to node 3.
		results in this trial are weird as the voltage and current jump off ~500% in the last ten minutes.


TRIPLEX_LINE CONDUCTOR:
		
	Triplex lines represent the distribution wires coming from the transformer into a typical residential home. That is, they 		are typically composed of one neutral wire and two "hot" wires. Triplex lines require the phase S to be specified as 			part of the phases parameter for proper implementation.
	
	LOOK AT " http://gridlab-d.sourceforge.net/wiki/index.php/Power_Flow_User_Guide#Triplex_Line_Configuration_Parameters  "



ASSERT MODEL:
	
	Assert objects work by taking a user defined value and comparing it against a property that is also specified by the user. There 	 are three different assert objects that may be used, complex_assert, double_assert, and enum_assert. These are used to test 		against complex numbers (r + j*x), double values (real numbers), and enumerations (strings), respectively. Each object also 		contains a number of operating modes that will further explained below.
	
	Look at " http://gridlab-d.sourceforge.net/wiki/index.php/Assert_(module)  "

