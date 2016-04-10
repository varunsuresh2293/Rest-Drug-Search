import json
import datetime
from pymongo import MongoClient
from bson import BSON
from bson import json_util
from bson import objectid
from flask import Flask,jsonify,request
from flask import Flask

app = Flask(__name__)

mongo_clinet= MongoClient("50.84.62.186",27017)
db=mongo_clinet.annt
db.authenticate("annt","5r4ShV7Z")


@app.route('/')
def hello_world():
    return 'Hello World!'

def del_none(d):
    dup=d.copy()
    """
    Delete keys with the value ``None`` in a dictionary, recursively.

    This alters the input so you may wish to ``copy`` the dict first.
    """
    if d is {} or (not len({})):
        return {"Result":"No Results To Display"}
    for key, value in d.items():
        if(value is None)or(value is '')or(value is "")or(not len(value)):
            del dup[key]
        elif isinstance(value, dict):
            del_none(value)
    return (dup)

def Fetch_drug_info_by_primaryid(drugname,primaryid):
    out=[]
    for record in db.DRUG13Q4.find({"$and":[{"primaryid":{"$in":primaryid},"drugname":drugname}]},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
            
    if out is None or (not len(out)):
        print("entered if loop")
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_demo_info_by_primaryid(drugname,primaryid):
    out=[]
    for record in db.DEMO13Q4.find({"primaryid":{"$in":primaryid}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)

    if out is None or (not len(out)):
        print("entered if loop")
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_indications_info_by_primaryid(drugname,primaryid):
    out=[]
    for record in db.INDI13Q4.find({"primaryid":{"$in":primaryid}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)

    if out is None or (not len(out)):
        print("entered if loop")
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_outcomes_info_by_primaryid(drugname,primaryid):
    out=[]
    for record in db.OUTC13Q4.find({"primaryid":{"$in":primaryid}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
    
    if out is None or (not len(out)):
        print("entered if loop")
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_reactions_info_by_primaryid(drugname,primaryid):
    out=[]
    for record in db.REAC13Q4.find({"primaryid":{"$in":primaryid}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
    if out is None or (not len(out)):
        print("entered if loop")
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_reports_info_by_primaryid(drugname,primaryid):
    out=[]
    for record in db.RPSR13Q4.find({"primaryid":{"$in":primaryid}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)

    if out is None or (not len(out)):
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_therapy_info_by_primaryid(drugname,primaryid):
    out=[]
    for record in db.THER13Q4.find({"primaryid":{"$in":primaryid}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
            
    if out is None or (not len(out)):
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_info_from_rxterms_by_rxcui(rxcui):
    out=[]
    for record in db.RxTerms201408.find({"RXCUI":{"$in":rxcui}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
    
    if out is None or (not len(out)):
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_info_from_rxtermsarchive_by_rxcui(rxcui):
    out=[]
    for record in db.RxTermsArchive201408.find({"RXCUI":{"$in":rxcui}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
            
    if out is None or (not len(out)):
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_info_from_rxtermsingredients_by_rxcui(rxcui):
    out=[]
    for record in db.RxTermsIngredients201408.find({"RXCUI":{"$in":rxcui}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
    
    if out is None or (not len(out)):
        out.append("No Results to Display")
        return out
    else:
        return out

def Fetch_info_from_NDF_public_tdu_by_id(NDF_id):
    out=[]
    for record in db["NDFRT_Public_2014.07.07_TDE"].find({"id":{"$in":NDF_id}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
    
    if out is None or (not len(out)):
        out.append("No Results to Display")
        return out
    else:
        return out


def Fetch_info_from_NDF_public_nui_by_id(name):
    out=[]
    for record in db["NDFRT_Public_NUI"].find({"CONCEPT_NAME":{"$in":name}},{"_id":0}):
        if record is None:
            out.append("No Results to Display")
            return out
        else:
            out.append(record)
    
    if out is None or (not len(out)):
        out.append("No Results to Display")
        return out
    else:
        return out




@app.route('/searchByDrugName/<drugname>')
def search_drug_by_name(drugname):
    primaryid=[]
    for record in db.DRUG13Q4.find({"drugname":drugname},{"primaryid":1,"_id":0}):
        primaryid.append(record["primaryid"])
    primaryid=sorted(list(set(primaryid)))
    infofromdrugtable=Fetch_drug_info_by_primaryid(drugname,primaryid)
    infofromdemotable=Fetch_demo_info_by_primaryid(drugname,primaryid)
    infofrominditable=Fetch_indications_info_by_primaryid(drugname,primaryid)
    infofromoutctable=Fetch_outcomes_info_by_primaryid(drugname,primaryid)
    infofromreactable=Fetch_reactions_info_by_primaryid(drugname,primaryid)
    infofromrpsrtable=Fetch_reports_info_by_primaryid(drugname,primaryid)
    infofromthertable=Fetch_therapy_info_by_primaryid(drugname,primaryid)
    results_from_drug_table="Results_From_FDA_Drug_Table_on_"+drugname
    results_from_demo_table="Results_From_FDA_Demo_Table_on_"+drugname
    results_from_indi_table="Results_From_FDA_Indications_Table_on_"+drugname
    results_from_outc_table="Results_From_FDA_Outcomes_Table_on_"+drugname
    results_from_reac_table="Results_From_FDA_Reactions_Table_on_"+drugname
    results_from_rpsr_table="Results_From_FDA_Reports_Table_on_"+drugname
    results_from_ther_table="Results_From_FDA_Therapy_Table_on_"+drugname
    FDARESULTS={results_from_drug_table:infofromdrugtable,
                results_from_demo_table:infofromdemotable,
                results_from_indi_table:infofrominditable,
                results_from_outc_table:infofromoutctable,
                results_from_reac_table:infofromreactable,
                results_from_rpsr_table:infofromrpsrtable,
                results_from_ther_table:infofromthertable
                }

    
    
    rxcuifromrxterms=[]
    rxcuifromrxtermsarchive=[]
    RXCUI=[]
    for record in db.RxTerms201408.find({"BRAND_NAME":drugname},{"RXCUI":1,"_id":0}):
        rxcuifromrxterms.append(record["RXCUI"])
    rxcuifromrxterms=sorted(list(set(rxcuifromrxterms)))
    for record in db.RxTermsArchive201408.find({"BRAND_NAME":drugname},{"RXCUI":1,"_id":0}):
        rxcuifromrxtermsarchive.append(record["RXCUI"])
    rxcuifromrxtermsarchive=sorted(list(set(rxcuifromrxtermsarchive)))
    
    for item  in rxcuifromrxterms:
        RXCUI.append(item)
    for item in rxcuifromrxtermsarchive:
        RXCUI.append(item)
    RXCUI=sorted(list(set(RXCUI)))
    infofromrxtermstable=Fetch_info_from_rxterms_by_rxcui(RXCUI)
    results_from_rxterms_table="Results_From_RX_RxTerms_Table_on_"+drugname
    infofromrxtermsarchivetable=Fetch_info_from_rxtermsarchive_by_rxcui(RXCUI)
    results_from_rxterms_archive_table="Results_From_RX_RxTerms_Archive_Table_on_"+drugname
    infofromrxtermsingredientstable=Fetch_info_from_rxtermsingredients_by_rxcui(RXCUI)
    results_from_rxterms_ingredients_table="Results_From_RX_RxTerms_Ingredients_Table_on_"+drugname
    RXRESULTS={
                results_from_rxterms_table:infofromrxtermstable,
                results_from_rxterms_archive_table:infofromrxtermsarchivetable,
                results_from_rxterms_ingredients_table:infofromrxtermsingredientstable
               }
    ING_RXCUI=[]
    for record in db.RxTermsIngredients201408.find({"RXCUI":{"$in":RXCUI}},{"ING_RXCUI\n":1,"_id":0}):
        ING_RXCUI.append(record["ING_RXCUI\n"])
    ING_RXCUI=sorted(list(set(ING_RXCUI)))
    infofromndftdutable=Fetch_info_from_NDF_public_tdu_by_id(ING_RXCUI)
    results_from_ndf_tdu_table="Results_From_NDF_Public_TDU_Table_on_"+drugname
    NAME=[]
    for record in db['NDFRT_Public_2014.07.07_TDE'].find({"id":{"$in":ING_RXCUI}},{"name":1,"_id":0}):
        NAME.append(record["name"])
    NAME=sorted(list(set(NAME)))
    infofromndfnuitable=Fetch_info_from_NDF_public_nui_by_id(NAME)
    results_from_ndf_nui_table="Results_From_NDF_Public_NUI_Table_on_"+drugname
    NDFRESULTS={
                results_from_ndf_tdu_table:infofromndftdutable,
                results_from_ndf_nui_table:infofromndfnuitable
                }
    result_from_fda_dataset="Results_From_FDA_DATASET_on_"+drugname+"_Table_wise"
    result_from_rx_dataset="Results_From_RX_DATASET_on_"+drugname+"_Table_wise"
    result_from_ndf_dataset="Results_From_NDF_DATASET_on_"+drugname+"_Table_wise"
    RESULTS={result_from_fda_dataset:FDARESULTS,
             result_from_rx_dataset:RXRESULTS,
             result_from_ndf_dataset:NDFRESULTS
            }
    sendtobrowser=json.dumps(RESULTS)
    return sendtobrowser


if __name__ == '__main__':
    app.run(debug=True)
