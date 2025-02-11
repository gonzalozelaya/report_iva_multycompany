# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ArgentinianReportCustomHandler(models.AbstractModel):
    _inherit = 'l10n_ar.tax.report.handler'
    
    @api.model
    def _vat_book_get_lines_domain(self, options):
        company_ids = self.env.companies.ids
        selected_journal_types = self._vat_book_get_selected_tax_types(options)
        domain = [('journal_id.type', 'in', selected_journal_types),
                  ('journal_id.l10n_latam_use_documents', '=', True), ('company_id', 'in', company_ids)]
        state = options.get('all_entries') and 'all' or 'posted'
        if state and state.lower() != 'all':
            domain += [('state', '=', state)]
        if options.get('date').get('date_to'):
            domain += [('date', '<=', options['date']['date_to'])]
        if options.get('date').get('date_from'):
            domain += [('date', '>=', options['date']['date_from'])]
        return domain