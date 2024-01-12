from odoo import models, fields, api

class grantmasteryproposals(models.Model):
    _inherit = 'crm.lead'
    _name = 'crm.lead'

    def _get_default_currency(self):
        usd_currency = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
        return usd_currency
    
    currency_field = fields.Many2one('res.currency', string='Currency', default=_get_default_currency)
        
    
    gm_type_of_cost_proposal = fields.Selection([
        ('fixed_fee', 'Fixed Fee'),
        ('percentage', 'Percentage'),
        # Add other options here
    ], string='Type of Cost Proposal')
    
    
    gm_tracking_number = fields.Char(string='Shipping Tracking Number')
    gm_texas_directory_phone_number = fields.Char(string='Texas Directory Phone Number')
    gm_template_documents_sent = fields.Boolean(string='Template Documents Sent')
    gm_submitted_proposal_filename = fields.Char(string='Filename for submitted proposal')
    gm_submitted_proposal = fields.Binary(string='Submitted Proposal', attachment=True)
    gm_rfprfq_filename = fields.Char(string='Filename for RFP/RFQ')
    gm_rfprfq_due_date = fields.Datetime(string='RFP/RFQ Due Date')
    gm_rfprfq = fields.Binary(string='RFP/RFQ', attachment=True)
    gm_proposal_sent = fields.Date(string='Proposal Sent')
    gm_proposal_received_documentation_filename = fields.Char(string='Filename for proposal received documentation')
    gm_proposal_received_documentation = fields.Binary(string='Proposal Received Documentation', attachment=True)
    gm_proposal_received = fields.Date(string='Proposal Received')
    gm_proposal_filename = fields.Char(string='Proposal')    
    gm_proposal = fields.Binary(string='Proposal', attachment=True)
    gm_procurement_lead = fields.Many2one('res.partner', string='LCMS Point of Contact')
    gm_notice_of_award_filename = fields.Char(string='Filename for notice of award')
    gm_notice_of_award = fields.Binary(string='Notice of Award', attachment=True)
    gm_ready_to_mail = fields.Datetime(string='Ready to Mail')
    
    
    gm_method_of_delivery = fields.Selection([
        ('email', 'Email'),
        ('online', 'Online Submission'),
        ('mail', 'Mail'),
        ('hand', 'Hand Delivery'),
    ], string='Method of Delivery', default='email')
    
    gm_mail_service = fields.Selection([
        ('usps', 'USPS'),
        ('ups', 'UPS'),
        ('fedex', 'FedEx'),
    ], string='Mail Service')
    
    gm_meeting_scheduled = fields.Datetime(string='Meeting Scheduled')
    gm_mail_proposal_to = fields.Text(string='Mail Proposal To:')
    gm_in_person_meeting = fields.Datetime(string='In-Person Meeting')
    gm_emailed_one_pager = fields.Datetime(string='Emailed One-Pager')
    gm_email_proposal_to = fields.Char(string='Email Proposal To')
    
    
    gm_competitor_awarded = fields.Selection([
        ('competitor1', 'Competitor 1'),
        ('competitor2', 'Competitor 2'),
        # Add other competitors here
    ], string='Competitor Awarded:')
    
    gm_competitor_awarded_user = fields.Many2one('res.partner', string='Competitor Awarded User')
    
    gm_award_amount = fields.Monetary(string='Competitor Award Amount', currency_field='currency_id')
    gm_administration_percentage = fields.Float(string='Administration Percentage')
    gm_addendum_2_filename = fields.Char(string='Filename for addendum_2')
    gm_addendum_2 = fields.Binary(string='Addendum #2', attachment=True)
    gm_addendum_1_filename = fields.Char(string='Filename for addendum_1')
    gm_addendum_1 = fields.Binary(string='Addendum #1', attachment=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.ref('base.USD'))
    gm_procurement_lead_1 = fields.Char(string='Procurement Lead Placeholder')
   
    
    