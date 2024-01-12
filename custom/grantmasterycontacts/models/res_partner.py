from odoo import models, fields, api, SUPERUSER_ID 
from odoo.exceptions import ValidationError
class ResPartner(models.Model):
    """
    This model extends the 'res.partner' model to represent a partner in the system with additional attributes specific to our use case.
    It includes various fields to store detailed information about the partner, such as their role, contact details, and project-related information.
    """

    _name = 'res.partner'
    _inherit = 'res.partner'
    
    company_type = fields.Selection(selection_add=[('company', 'Organization')])

    def _get_default_currency(self):
        usd_currency = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
        return usd_currency
    
    currency_field = fields.Many2one('res.currency', string='Currency', default=_get_default_currency)
    
    # Indicates if the partner is a contact in the Texas Directory.
    gm_texas_directory_contact = fields.Boolean(string='Texas Directory Contact', default=False)
    gm_texas_directory_update = fields.Date(string= 'Texas Directory Update')
    
    # Specifies the type of organization, with options like city, county, school district, etc.
    gm_organization_type = fields.Selection([
        ('city', 'City'),
        ('county', 'County'),
        ('cog', 'Council of Government (COG)'),
        ('town', 'Town'),
        ('village', 'Village'),
        ('cdp', 'Census Designated Place (CDP)'),
        ('grant_company', 'Grant Company'),
        ('state_agency', 'State Agency'),
        ('federal_agency', 'Federal Agency'),
        ('regional_planning_organization', 'Regional Planning Organization'),
        ('engineering_company', 'Engineering Company'),
        ('construction_company', 'Construction Company'),
        ('acquisition_company', 'Acquisition Company'),
        ('nonprofit', 'Nonprofit'),
        ('business', 'Business'),
        ('school', 'School District'),
        ('wsc', 'Water Supply Corporation (WSC)'),
        ('ud', 'Utility District'),
        ('sd', 'Special District'),
        ('other', 'Other'),
    ], string='Organization Type')
    
    gm_community_type = fields.Selection([
        ('city', 'City'),
        ('county', 'County'),
        ('town', 'Town'),
        ('village', 'Village'),
        ('cdp', 'Census Designated Place (CDP)'),
    ], string='Community Type')
    
    gm_current_client = fields.Boolean(string='Current Client', default=False)

    # Relates project managers to the partner, allowing for many-to-many relationships.
    project_manager_ids = fields.Many2many(
        'res.partner', 
        'partner_project_manager_rel', 
        'partner_id', 
        'project_manager_id', 
        string='Project Managers', 
    )
    
    gm_community_type = fields.Selection([
        ('city', 'City'),
        ('county', 'County'),
        ('town', 'Town'),
        ('village', 'Village'),
        ('cdp', 'Census Designated Place (CDP)'),
    ], string='Community Type')

    gm_is_community = fields.Boolean(string='Is Community', default=False)
    
    # Relates project managers to the partner, allowing for many-to-many relationships.
    project_manager_ids = fields.Many2many(
        'res.partner', 
        'partner_project_manager_rel', 
        'partner_id', 
        'project_manager_id', 
        string='Project Managers', 
    )
    
    # Fields for the plannning & plans page
    gm_comprehensive_plan = fields.Binary(string='Comprehensive Plan', attachment=True)
    gm_comprehensive_plan_filename = fields.Char(string='Comprehensive Plan Filename')
    gm_comprehensive_plan_adoption_date = fields.Date(string='Comprehensive Plan Adoption Date')
    
    gm_hmp_plan = fields.Binary(string='Hazard Mitigation Plan (HMP)', attachment=True)
    gm_hmp_plan_filename = fields.Char(string='Hazard Mitigation Plan Filename')
    gm_hmp_adoption_date = fields.Date(string='HMP Adoption Date')
    gm_hmp_exp_date = fields.Date(string='HMP Expiration Date')
   
    gm_land_use_plan = fields.Binary(string='Land Use Plan', attachment=True)
    gm_land_use_plan_filename = fields.Char(string='Land Use Plan Filename')
    gm_land_use_map = fields.Binary(string='Land Use Map', attachment=True)
    gm_land_use_map_filename = fields.Char(string='Land Use Map Filename')
    gm_land_use_plan_adoption_date = fields.Date(string='Land Use Plan Adoption Date')
   
    gm_cwpp_plan = fields.Binary(string='Community Wildfire Protection Plan', attachment=True)
    gm_cwpp_plan_filename = fields.Char(string='Community Wildfire Protection Plan Filename')  
    gm_cwpp_adoption_date = fields.Date(string='CWPP Adoption Date')
    gm_cwpp_exp_date = fields.Date(string='CWPP Expiration Date')   
    
    gm_transportation_plan = fields.Binary(string='Transportation Plan', attachment=True)
    gm_transportation_plan_filename = fields.Char(string='Transportation Plan Filename')
    gm_transportation_plan_adoption_date = fields.Date(string='Transportation Plan Adoption Date')
    
    gm_drainage_plan = fields.Binary(string='Drainage Plan', attachment=True)
    gm_drainage_plan_filename = fields.Char(string='Drainage Plan Filename')
    gm_drainage_plan_adoption_date = fields.Date(string='Drainage Plan Adoption Date')
    
    gm_parks_plan = fields.Binary(string='Parks Plan', attachment=True)
    gm_parks_plan_filename = fields.Char(string='Parks Plan Filename')
    gm_parks_plan_adoption_date = fields.Date(string='Parks Plan Adoption Date')
    
    gm_economic_development_plan = fields.Binary(string='Economic Development Plan', attachment=True)
    gm_economic_development_plan_filename = fields.Char(string='Economic Development Plan Filename')
    gm_economic_development_plan_adoption_date = fields.Date(string='Economic Development Plan Adoption Date')
    
    gm_capital_improvement_plan = fields.Binary(string='Capital Improvement Plan', attachment=True)
    gm_capital_improvement_plan_filename = fields.Char(string='Capital Improvement Plan Filename')
    gm_capital_improvement_plan_adoption_date = fields.Date(string='Capital Improvement Plan Adoption Date')
    
    gm_asset_management_plan = fields.Binary(string='Asset Management Plan', attachment=True)
    gm_asset_management_plan_filename = fields.Char(string='Asset Management Plan Filename')
    gm_asset_management_plan_adoption_date = fields.Date(string='Asset Management Plan Adoption Date')
    
    transportation_safety_plan = fields.Binary(string='Transportation Safety Plan', attachment=True)
    transportation_safety_plan_filename = fields.Char(string='Transportation Safety Plan Filename')
    transportation_safety_plan_adoption_date = fields.Date(string='Transportation Safety Plan Adoption Date')
    
    
    gm_downtown_plan = fields.Binary(string='Downtown Plan', attachment=True)
    gm_downtown_plan_filename = fields.Char(string='Downtown Plan Filename')
    gm_downtown_plan_adoption_date = fields.Date(string='Downtown Plan Adoption Date')
    
    gm_population_study = fields.Binary(string='Population Study', attachment=True)
    gm_population_study_filename = fields.Char(string='Population Study Filename')
    gm_population_study_date = fields.Date(string='Population Study Date')
    
    gm_housing_study = fields.Binary(string='Housing Study', attachment=True)
    gm_housing_study_filename = fields.Char(string='Housing Study Filename')
    gm_housing_study_date = fields.Date(string='Housing Study Date')
    
    
    gm_zoning_ordiance = fields.Binary(string='Zoning Ordinance', attachment=True)
    gm_zoning_ordiance_filename = fields.Char(string='Zoning Ordinance Filename')
    gm_zoning_ordiance_adoption_date = fields.Date(string='Zoning Ordinance Adoption Date')
    gm_zoning_map = fields.Binary(string='Zoning Map', attachment=True)
    gm_zoning_map_filename = fields.Char(string='Zoning Map Filename')
    gm_zoning_ordinace_adoption_date = fields.Date(string='Zoning Ordinance Adoption Date')
    
    gm_building_code_ordiance = fields.Binary(string='Building Code Ordinance', attachment=True)
    gm_building_code_ordiance_filename = fields.Char(string='Building Code Ordinance Filename')
    gm_building_code_ordiance_adoption_date = fields.Date(string='Building Code Adoption Date')
    gm_Building_code_standard = fields.Selection([
        ('ibc_2000', 'IBC 2000'),
        ('ibc_2003', 'IBC 2003'),
        ('ibc_2006', 'IBC 2006'),
        ('ibc_2009', 'IBC 2009'),
        ('ibc_2012', 'IBC 2012'),
        ('ibc_2015', 'IBC 2015'),
        ('ibc_2018', 'IBC 2018'),
        ('ibc_2021', 'IBC 2021'),
        ('other', 'Other'),
    ], string='IBC Standard')
        
    gm_irc_ordiance = fields.Binary(string='International Residentail Code (IRC) Ordinance', attachment=True)
    gm_irc_ordiance_filename = fields.Char(string='International Residentail Code (IRC) Ordinance Filename')
    gm_irc_ordiance_adoption_date = fields.Date(string='IRC Adoption Date') 
    gm_irc_standard = fields.Selection([
        ('irc_2000', 'IRC 2000'),
        ('irc_2006', 'IRC 2006'),
        ('irc_2012', 'IRC 2012'),
        ('irc_2015', 'IRC 2015'),
        ('irc_2021', 'IRC 2021'),
        ('other', 'Other'),
    ], string='IRC Standard')
    
    gm_ipmc_ordiance = fields.Binary(string='International Property Maintenance Code (IPMC) Ordinance', attachment=True)
    gm_ipmc_ordiance_filename = fields.Char(string='International Property Maintenance Code (IPMC) Ordinance Filename')
    gm_ipmc_ordiance_adoption_date = fields.Date(string='IPMC Adoption Date')
    gm_ipmc_standard = fields.Selection([
        ('ipmc_2009', 'IPMC 2009'),
        ('ipmc_2012', 'IPMC 2012'),
        ('ipmc_2015', 'IPMC 2015'),
        ('ipmc_2021', 'IPMC 2021'),
        ('other', 'Other'),
    ], string='IPMC Standard') 
           
    gm_plumbing_ordiance = fields.Binary(string='Uniform Plumbing Code (UPC) Ordinance', attachment=True)
    gm_plumbing_ordiance_filename = fields.Char(string='Uniform Plumbing Code (UPC) Ordinance Filename')
    gm_plumbing_ordiance_adoption_date = fields.Date(string='UPC Ordinance Adoption Date')
    gm_plumbing_standard = fields.Selection([
        ('upc_2003', 'UPC 2003'),
        ('upc_2009', 'UPC 2009'),
        ('upc_2012', 'UPC 2012'),
        ('upc_2015', 'UPC 2015'),
        ('upc_2021', 'UPC 2021'),
        ('other', 'Other'),
    ], string='UPC Standard')
    
    gm_mechanical_ordiance = fields.Binary(string='Uniform Mechanical Code (UMC) Ordinance', attachment=True)
    gm_mechanical_ordiance_filename = fields.Char(string='Uniform Mechanical Code (UMC) Ordinance Filename')
    gm_mechanical_ordiance_adoption_date = fields.Date(string='UMC Adoption Date')
    gm_mechanical_standard = fields.Selection([
        ('umc_2003', 'UMC 2003'),
        ('umc_2009', 'UMC 2009'),
        ('umc_2012', 'UMC 2012'),
        ('umc_2015', 'UMC 2015'),
        ('umc_2021', 'UMC 2021'),
        ('other', 'Other'),
    ], string='UMC Standard')
    
    gm_electrical_ordiance = fields.Binary(string='National Electrical Code (NEC) Ordinance', attachment=True)
    gm_electrical_ordiance_filename = fields.Char(string='National Electrical Code (NEC) Ordinance Filename')
    gm_electrical_ordiance_adoption_date = fields.Date(string='NEC Adoption Date')
    gm_electrical_ordiance_standard = fields.Selection([
        ('nec_2002', 'NEC 2002'),
        ('nec_2005', 'NEC 2005'),
        ('nec_2008', 'NEC 2008'),
        ('nec_2011', 'NEC 2011'),
        ('nec_2014', 'NEC 2014'),
        ('nec_2017', 'NEC 2017'),
        ('nec_2020', 'NEC 2020'),
        ('other', 'Other'),
    ], string='NEC Standard')
    
    gm_fire_code_ordiance = fields.Binary(string='International Fire Code (IFC) Ordinance', attachment=True)
    gm_fire_code_ordiance_filename = fields.Char(string='International Fire Code (IFC) Ordinance Filename')
    gm_fire_code_ordiance_adoption_date = fields.Date(string='IFC Ordinance Adoption Date')
    gm_fire_code_standard = fields.Selection([
        ('ifc_2003', 'IFC 2003'),
        ('ifc_2009', 'IFC 2009'),
        ('ifc_2012', 'IFC 2012'),
        ('ifc_2015', 'IFC 2015'),
        ('ifc_2021', 'IFC 2021'),
        ('other', 'Other'),
    ], string='IFC Standard')
    
    gm_wildland_urban_interface_code_ordiance = fields.Binary(string='International Wildland-Urban Interface Code (IWUIC) Ordinance', attachment=True) 
    gm_wildland_urban_interface_code_ordiance_filename = fields.Char(string='International Wildland-Urban Interface Code (IWUIC) Ordinance Filename')
    gm_wildland_urban_interface_code_ordiance_adoption_date = fields.Date(string='IWUIC Adoption Date')
    gm_wildland_urban_interface_code_standard = fields.Selection([
        ('iwuic_2020', 'IWUIC 2020'),
        ('other', 'Other'),
    ], string='IWUIC Standard')
    
    gm_energy_conservation_code_ordiance = fields.Binary(string='International Energy Conservation Code (IECC) Ordinance', attachment=True)
    gm_energy_conservation_code_ordiance_filename = fields.Char(string='IECC Ordinance Filename')
    gm_energy_conservation_code_ordiance_adoption_date = fields.Date(string='IECC Adoption Date')
    gm_energy_conservation_code_standard = fields.Selection([
        ('iecc_2000', 'IECC 2000'),
        ('iecc_2006', 'IECC 2006'),
        ('iecc_2009', 'IECC 2009'),
        ('iecc_2012', 'IECC 2012'),
        ('iecc_2015', 'IECC 2015'),
        ('iecc_2021', 'IECC 2021'),
        ('other', 'Other'),
    ], string='IECC Standard')
        
    gm_solar_ordinance = fields.Binary(string='Solar Code Ordinance', attachment=True)
    gm_solar_ordinance_filename = fields.Char(string='Solar Code Ordinance Filename')
    gm_solar_ordinance_adoption_date = fields.Date(string='Solar Adoption Date')
    gm_solar_standard = fields.Selection([
        ('usec_1984', 'USEC 1984'),
        ('usec_1997', 'USEC 1997'),
        ('usec_1988', 'USEC 1988'),
        ('usec_2006', 'USEC 2006'),
        ('other', 'Other'),
    ], string='Solar Code Standard')
    
        
    
    # Fields to store various regulatory and statistical data.
    gm_sam_registration_filename = fields.Char(string='SAM Registration Filename')
    gm_sam_registration = fields.Binary(string='SAM Registration')
    gm_sams_expiration = fields.Date(string='SAMs Expiration')
    gm_census_geoid = fields.Char(string='Census GEOID')
    gm_fema_cid = fields.Char(string='FEMA CID')
    gm_lmi_2021 = fields.Float(string='2021 LMI%', digits=(3, 2))
    gm_glo_mit_lmi = fields.Float(string='GLO MIT LMI%', digits=(3, 2))
    gm_lmi_2023 = fields.Float(string='2023 LMI%', digits=(3, 2))
    gm_tax_id_prefix = fields.Char(string='Tax ID Prefix')
    gm_state_tin = fields.Char(string='State TIN')
    gm_uei = fields.Char(string='UEI')
    gm_duns = fields.Char(string='DUNS')
    gm_fips = fields.Char(string='FIPS')
    gm_fy_end = fields.Date(string='Fiscal Year End')
    gm_namelsad = fields.Char(string='NameLSAD')
    gm_cog = fields.Char(string='COG')
    gm_county = fields.Char(string='County')
    gm_council_schedule = fields.Char(string='Council Schedule')
    gm_court_schedule = fields.Char(string='Court Schedule')
    gm_po_box = fields.Char(string='PO Box')
    gm_amhi_22 = fields.Char(string='AMHI 2022')
    gm_amhi_percent_22 = fields.Float(string='AMHI 2022 %', digits=(3, 1))
    gm_tx_directory_cityid = fields.Char(string='TX Directory CityID')
    gm_tx_directory_offholder_id = fields.Char(string='TX Directory OffholderID')
    gm_tx_directory_phone = fields.Char(string='TX Directory Phone')
    gm_tx_directory_email = fields.Char(string='TX Directory Email')   
    gm_2020_census_tracts = fields.Text(string='2020 Census Tracts')
    # gm_wkt_geometry = fields.Text(string='WKT Geometry')
   
    # # Fields for FEMA Grants
    gm_nri_risk_score = fields.Float(string='NRI Risk Score', digits=(3, 2))
    gm_nri_risk_rating = fields.Selection([
        ('very_high', 'Very High'),
        ('relatively_high', 'Relatively High'),
        ('relatively_moderate', 'Relatively Moderate'),
        ('relatively_low', 'Relatively Low'),
        ('very_low', 'Very Low'),
        ('insufficient_data', 'Insufficient Data'),
    ], string='NRI Risk Rating')
    gm_overlap_3xsvi = fields.Float(string='Overlap Percentage 3xSVI 2023', digits=(3, 2))
    gm_cejst_underserved_census_tracts = fields.Text(string='CJEST Underserved Census Tracts')
    gm_overlap_cejst_underserved_census_tracts = fields.Float(string='Overlap Percentage CJEST Underserved Census Tracts', digits=(3, 2))
    gm_nfip_community = fields.Boolean(string='NFIP Community', default=False)
    gm_crs_class = fields.Integer(string='CRS Class')
    gm_repetitive_loss_structures = fields.Integer(string='Repetitive Loss Structures')
    gm_severe_repetitive_loss_structures = fields.Integer(string='Severe Repetitive Loss Structures')

    
    
    
    @api.depends('is_company')
    def _compute_company_type(self):
        for partner in self:
            partner.company_type = 'company' if partner.is_company else 'person'

    def _write_company_type(self):
        for partner in self:
            partner.is_company = partner.company_type == 'company'

    @api.onchange('company_type')
    def onchange_company_type(self):
        self.is_company = (self.company_type == 'company')
   
#     def migrate(cr, version):
#         env = api.Environment(cr, SUPERUSER_ID, {})
#         partner_model = env['res.partner']
#  # Adding fields using Odoo ORM
#         partner_model._add_field('gm_wkt_geometry', fields.Text(string='WKT Geometry'))


